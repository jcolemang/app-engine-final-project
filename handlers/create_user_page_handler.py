
from base_handler import BaseHandler
from models import User

from google.appengine.api import users
from webapp2 import RequestHandler


class CreateUserPageHandler(BaseHandler):

    template_name = 'create-user-page/create-user-page.html'

    def get(self):
        auth_user = self.get_auth_user()
        template = self.get_template()
        values = {
            'logout_url': users.create_logout_url(auth_user),
        }
        self.response.write(template.render(values))


    def post(self):
        username = self.request.get('username-input')
        email = users.get_current_user().email().lower()

        user = User(username=username,
                    email=email,
                    calendars_following=[])
        user.put()

        self.redirect('/')


    def get_template(self):
        return self.get_template_by_name(CreateUserPageHandler.template_name)
