#!/usr/bin/env python2

import webapp2
import jinja2
import os
import json
from rosefire import RosefireTokenVerifier

from webapp2_extras import sessions
from handlers.calendar_page_handler import CalendarPageHandler, GenerateDatesHandler
from handlers.create_user_page_handler import CreateUserPageHandler
from handlers.dashboard_page_handler import DashboardPageHandler


# This normally shouldn't be checked into Git
ROSEFIRE_SECRET = '9DYUFGrQ1QvYMtsrm56V'

config = {}
config["webapp2_extras.sessions"] = {
    'secret_key': '9DYUFGrQ1QvYMtsrm56V'}

JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True)

# From: https://webapp2.readthedocs.io/en/latest/api/webapp2_extras/sessions.html
class BaseHandler(webapp2.RequestHandler):
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

class MainHandler(BaseHandler):
    def get(self):
        template = JINJA_ENV.get_template("templates/index.html.jinja")
        if "user_info" in self.session:
          user_info = json.loads(self.session["user_info"])
          print("user_info", user_info)
          self.response.out.write(template.render({"user_info": user_info}))
        else:
          self.response.out.write(template.render())

class LoginHandler(BaseHandler):
    def get(self):
        if "user_info" not in self.session:
            token = self.request.get('token')
            auth_data = RosefireTokenVerifier(ROSEFIRE_SECRET).verify(token)
            user_info = {"name": auth_data.name,
                         "username": auth_data.username,
                         "email": auth_data.email,
                         "role": auth_data.group}
            self.session["user_info"] = json.dumps(user_info)
        self.redirect(uri="/dashboard")

class LogoutHandler(BaseHandler):
    def get(self):
        del self.session["user_info"]
        self.redirect(uri="/")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/dashboard', DashboardPageHandler),
    ('/calendar/(.*)/(.*)', CalendarPageHandler),
    ('/generate-calendar', GenerateDatesHandler),
], debug=True)
