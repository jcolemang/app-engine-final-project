from handlers.base_handler import BaseHandler
from rosefire import RosefireTokenVerifier

import json

# This normally shouldn't be checked into Git
ROSEFIRE_SECRET = 'Pho4xZW6cOebVlK0hcDQ'

config = {}
config["webapp2_extras.sessions"] = {
    'secret_key': 'Pho4xZW6cOebVlK0hcDQ'}

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
      
        self.redirect(uri="/")

config = {}
config['webapp2_extras.sessions'] = {
    # This key is used to encrypt your sessions
    'secret_key': 'mysecretkey',
}