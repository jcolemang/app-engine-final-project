
from base_handler import BaseHandler
import utils
import re

from google.appengine.api import users


class DashboardPageHandler(BaseHandler):

    template_name = 'dashboard-page/dashboard-page.html'
    valid_name_re = re.compile(r'^\w+$')


    def calendar_name_is_valid(self, name):
        return DashboardPageHandler.valid_name_re.match(name) and True

    def get_template(self):
        return self.get_template_by_name(DashboardPageHandler.template_name)


    def add_values(self, values):
        values['calendar_query'] = utils.query_user_calendars(values['email'])


    def handle_post(self, user):
        auth_user = users.get_current_user()
        email = auth_user.email().lower()

        calendar_name = self.request.get('calendar-name')
        if not self.calendar_name_is_valid(calendar_name):
            # TODO deal with this
            return False

        calendar = utils.create_default_calendar(user, calendar_name)
        self.redirect('/calendar/%s/%s' % (user.username, calendar_name))
