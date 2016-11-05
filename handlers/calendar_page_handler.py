from google.appengine.api import users
from google.appengine.ext import ndb

from base_handler import BaseHandler
from models import CalendarRow
import utils


class CalendarPageHandler(BaseHandler):

    template_name = 'calendar-page/calendar-page.html'

    def get(self, username, calendar_name):
        auth_user = users.get_current_user()
        email = self.get_auth_user_email(auth_user)
        user = utils.get_user_from_email(email)
        values = self.get_base_values(auth_user, user)

        calendar_user = utils.get_user_from_username(username)
        calendar = utils.get_calendar(calendar_user, calendar_name)

        values['calendar'] = calendar
        values['user_owns_calendar'] = calendar.owner == user.key

        template = self.get_template()
        self.response.write(template.render(values))


    def put(self, username, calendar_name):
        text = self.request.get('text')
        url_safe_key = self.request.get('url_safe_key')
        key = ndb.Key(urlsafe=url_safe_key)
        cell = key.get()
        cell.text = text
        cell.put()
        values = {'success': True}
        self.response.write(values)


    def post(self, username, calendar_name):
        add_after_key_urlsafe = self.request.get('addAfter')
        user = utils.get_user_from_username(username)
        calendar = utils.get_calendar(user, calendar_name)
        num_columns = len(calendar.column_names)

        if add_after_key_urlsafe == 'last-row':
            row_index = len(calendar.row_keys)
        else:
            add_after_key = ndb.Key(urlsafe=add_after_key_urlsafe)
            row_index = calendar.row_keys.index(add_after_key)

        utils.insert_row(calendar, user, row_index)
        self.response.write('it worked')


    def get_template(self):
        return self.get_template_by_name(CalendarPageHandler.template_name)


    def add_values(self, values):
        pass
