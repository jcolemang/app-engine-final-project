from google.appengine.api import users
from google.appengine.ext import ndb
import json
from datetime import date, timedelta, datetime

from base_handler import BaseHandler, UnauthorizedException
from models import CalendarRow
import utils



class GenerateDatesHandler(BaseHandler):


    def get(self):
        raise UnauthorizedException('Page does not support get requests')


    def post(self):

        # checking authentication
        auth_user = self.get_auth_user()
        auth_user_email = self.get_auth_user_email(auth_user)
        user = utils.get_user_from_email(auth_user_email)
        calendar_username = self.request.get('username')
        if user.username != calendar_username:
            raise Exception('Change this to be more specific')

        # helpers
        date_format = '%Y-%m-%d'
        str_to_date = lambda d, s: datetime.strptime(d, s).date()

        # getting user input
        calendar_name = self.request.get('calendarName')
        num_days = int(self.request.get('numDays'))
        str_vacation_ranges = json.loads(self.request.get('vacationRanges'))
        str_start_date = self.request.get('startDate')

        # converting user input
        start_date = str_to_date(str_start_date, date_format)
        vacation_date_pairs = map(lambda pair: \
                                  map(lambda d: \
                                      str_to_date(d, date_format), \
                                      pair), \
                                  str_vacation_ranges)

        session_dates = self.get_session_dates(num_days,
                                               start_date,
                                               vacation_date_pairs)

        # inserting the rows
        calendar = utils.get_calendar(user, calendar_name)
        calendar_row_keys = calendar.row_keys
        calendar_rows = map(lambda k: k.get(), calendar_row_keys)
        self.update_dates_and_add_rows(calendar_rows, session_dates, calendar, user)

        self.response.out.write('wow!')


    def update_dates_and_add_rows(self, rows, dates, calendar, user):

        rows.sort(key=lambda row: row.date_cell.get().date)
        update_start = 0
        insert_start = min(len(rows), len(dates))

        # updating existing rows
        for row_num in range(update_start, min(len(rows), len(dates))):
            row = rows[row_num]
            date = dates[row_num]
            date_cell = row.date_cell.get()
            date_cell.date = date
            date_cell.put()

        # adding new rows
        for date_num in range(insert_start, len(dates)):
            utils.insert_row(calendar, user, dates[date_num])


    def get_session_dates(self, num_sessions, start_date, vacation_ranges):

        dates = []
        one_day = timedelta(days=1)
        curr_sessions = 0
        between_dates = lambda d, start, end: start <= d <= end
        is_weekend = lambda d: d.weekday() in [5, 6]
        curr_date = start_date

        while len(dates) < num_sessions:

            is_a_weekend = is_weekend(curr_date)
            is_in_a_vacation = reduce(lambda b1, b2: b1 or b2,
                                      map(lambda pair: \
                                          between_dates(curr_date,
                                                        pair[0],
                                                        pair[1]),
                                          vacation_ranges),
                                      False)
            is_valid = not (is_in_a_vacation or is_a_weekend)

            if is_valid:
                dates.append(curr_date)

            curr_date = curr_date + one_day

        return dates


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


    def delete(self, username, calendar_name):
        user = utils.get_user_from_username(username)
        calendar = utils.get_calendar(user, calendar_name)
        url_safe_row_key = self.request.get('rowKey')
        row_key = ndb.Key(urlsafe=url_safe_row_key)
        utils.delete_row(calendar, row_key)
        self.response.write('deleted')


    def get_template(self):
        return self.get_template_by_name(CalendarPageHandler.template_name)


    def add_values(self, values):
        pass
