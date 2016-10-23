from google.appengine.api import users

from base_handler import BaseHandler
import utils


class CalendarPageHandler(BaseHandler):

    template_name = 'calendar-page/calendar-page.html'

    def get(self, username, calendar_name):
        auth_user = users.get_current_user()
        user = utils.get_curr_user_from_username(username)
        values = self.get_base_values(auth_user, user)

        calendar = utils.get_calendar(user, calendar_name)
        values['calendar'] = calendar

        template = self.get_template()
        self.response.write(template.render(values))


    def get_template(self):
        return self.get_template_by_name(CalendarPageHandler.template_name)


    def add_values(self, values):
        pass
