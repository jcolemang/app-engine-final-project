
from base_handler import BaseHandler
from models import Calendar

from google.appengine.api import users


class DashboardPageHandler(BaseHandler):

    template_name = 'dashboard-page/dashboard-page.html'

    def get_template(self):
        return self.get_template_by_name(DashboardPageHandler.template_name)

    def add_values(self, values):
        curr_user = users.get_current_user()
        values['email'] = curr_user.email().lower()

    def handle_post(self, user):
        print '\n', user.key, '\n'
        self.redirect('/')
