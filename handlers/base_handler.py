
import os

from google.appengine.api import users
from jinja2 import Environment, FileSystemLoader
from webapp2 import RequestHandler

from models import User
import utils


class BaseHandler(RequestHandler):

    # setting the environment
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    env = Environment(loader=FileSystemLoader([template_path]))
    template_name = None


    def get_auth_user(self):
        auth_user = users.get_current_user()
        if not auth_user:
            raise Exception('User not logged in')
        return auth_user


    def get(self):
        auth_user = self.get_auth_user()
        template = self.get_template()
        values = self.get_base_values(auth_user.email())
        self.add_values(values)
        self.response.write(template.render(values))


    def post(self):
        auth_user = self.get_auth_user()
        if not auth_user:
            raise Exception('User not logged in')
        user_email = auth_user.email().lower()
        curr_user = utils.get_curr_user_from_email(user_email)
        self.handle_post(curr_user)


    def handle_post(self, user):
        raise Exception('Must override handle_post')


    def get_template_by_name(self, template_name):
        return self.get_env().get_template(template_name)


    def get_template(self):
        raise RuntimeError('Must override get_template')


    def get_base_values(self, email):
        return {
            'path': self.request.path,
            'user': utils.get_curr_user_from_email(email)
        }


    def add_values(self, values):
        pass


    def get_env(self):
        return BaseHandler.env
