
from base_handler import BaseHandler
import utils

from google.appengine.api import users


class DashboardPageHandler(BaseHandler):

    template_name = 'dashboard-page/dashboard-page.html'

    def get_template(self):
        return self.get_template_by_name(DashboardPageHandler.template_name)


    def add_values(self, values):
        values['calendar_query'] = utils.query_user_calendars(values['email'])


    def handle_post(self, user):
        auth_user = users.get_current_user()
        email = auth_user.email().lower()

        calendar_name = self.request.get('calendar-name')
        calendar = utils.put_calendar_for_user(email, calendar_name)

        self.redirect('/')
