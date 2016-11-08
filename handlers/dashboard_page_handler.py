
import utils
import re
from google.appengine.api import users

from base_handler import BaseHandler
from models import RepeatCalendarException


class DashboardPageHandler(BaseHandler):

    template_name = 'dashboard-page/dashboard-page.html'
    valid_name_re = re.compile(r'^[a-zA-Z\-0-9_]+$$')


    def calendar_name_is_valid(self, name):
        return DashboardPageHandler.valid_name_re.match(name) and True

    def get_template(self):
        return self.get_template_by_name(DashboardPageHandler.template_name)


    def add_values(self, values):
        values['calendar_query'] = utils.query_user_calendars(values['email'])


    def handle_post(self, user):
        calendar_name = self.request.get('calendarName')
        if not self.calendar_name_is_valid(calendar_name):
            self.redirect('/')
            return False

        try:
            calendar = utils.create_default_calendar(user, calendar_name)
        except RepeatCalendarException:
            self.response.out.write('calendarexists')
            return

        self.response.write('/calendar/%s/%s' % (user.username, calendar_name))


    def delete(self):
        auth_user = self.get_auth_user()
        user_email = self.get_auth_user_email(auth_user)
        user = utils.get_user_from_email(user_email)
        calendar_name = self.request.get('calendarName')
        utils.delete_calendar(user, calendar_name)
        self.response.write('deleted')
