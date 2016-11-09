import os
import json

from google.appengine.api import users
from jinja2 import Environment, FileSystemLoader
from webapp2 import RequestHandler
import webapp2
from webapp2_extras import sessions

import utils


# This normally shouldn't be checked into Git
ROSEFIRE_SECRET = 'Pho4xZW6cOebVlK0hcDQ'

config = {}
config["webapp2_extras.sessions"] = {
    'secret_key': 'Pho4xZW6cOebVlK0hcDQ'}

class UnauthorizedException(Exception):
    pass


class BaseHandler(RequestHandler):

    # setting the environment
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    env = Environment(loader=FileSystemLoader([template_path]))
    template_name = None
    
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()


    def get_auth_user(self):
      if "user_info" in self.session:
              tempdata = json.loads(self.session["user_info"])
      #         tempdata = json.loads(self.session)
              email = tempdata['email']
              user = utils.get_user_from_email(email)
              return user
            
      else:
      #         user = utils.create_user(email)
          self.redirect(uri="/blank")
          return False;


    def get_auth_user_email(self, auth_user):
         return self.get_auth_user().email


    def get(self):    
#       auth_user = self.get_auth_user()
      if "user_info" in self.session:
        tempdata = json.loads(self.session["user_info"])
#         tempdata = json.loads(self.session)
        email = tempdata['email']
        user = utils.get_user_from_email(email)
      
      else:
#         user = utils.create_user(email)
          self.redirect(uri="/blank")
          return
           
      template = self.get_template()
      values = self.get_base_values("", user)
      self.add_values(values)
      self.response.write(template.render(values))


    def post(self):
        auth_user = self.get_auth_user()
        user_email = auth_user.email
        curr_user = utils.get_user_from_email(user_email)
        self.handle_post(curr_user)


    def handle_post(self, user):
        raise Exception('Must override handle_post')


    def get_template_by_name(self, template_name):
        return self.get_env().get_template(template_name)


    def get_template(self):
        raise RuntimeError('Must override get_template')


    def get_base_values(self, auth_user, user):
        return {
            'user_info': self.session["user_info"],
            'path': self.request.path,
            'user': user,
            'username': user.username,
            'email': user.email,
            'logout_url': users.create_logout_url('/logout'),
            'date_format': '%a, %b %e'
        }


    def add_values(self, values):
        pass


    def get_env(self):
        return BaseHandler.env

config = {}
config['webapp2_extras.sessions'] = {
    # This key is used to encrypt your sessions
    'secret_key': 'mysecretkey',
}
