from google.appengine.ext import ndb
import re

from models import User, Calendar, Cell, DoesNotExistError, CalendarRow, RepeatCalendarException

# some constants
username_re = re.compile('(.*)@.*')


def get_parent_key_for_email(email):
    return ndb.Key("Entity", email.lower())


def put_calendar_for_user(email, calendar_name):
    user = get_curr_user_from_email(email)
    calendar = Calendar(parent=user.key,
                        name=calendar_name,
                        owner=user.key)
    calendar.put()
    return calendar


def create_default_calendar(current_user, name):
    try:
        get_calendar(current_user, name)
        raise RepeatCalendarException('Calendar already exists')
    except DoesNotExistError:
        pass

    # creating the actual calendar object
    calendar = Calendar(parent=current_user.key,
                        owner=current_user.key,
                        name=name)
    calendar.column_names = Calendar.default_columns
    calendar.put()
    append_calendar_row(calendar, current_user)
    return calendar


def append_calendar_row(calendar, current_user, num_columns=None):
    if not num_columns:
        num_columns = len(calendar.column_names)

    row = CalendarRow(parent=calendar.key)
    row.put()

    cell_keys = []
    for i in range(num_columns):
        cell = Cell(parent=row.key)
        cell.put()
        cell_keys.append(cell.key)

    row.cell_keys = cell_keys
    row.put()
    print row.cell_keys

    calendar.row_keys.append(row.key)
    calendar.put()


def query_user_calendars(email):
    user = get_curr_user_from_email(email)
    calendar_query = Calendar.query(ancestor=user.key)\
                             .order(Calendar.name)
    return calendar_query


def get_calendar(user, calendar_name):
    cal_query = Calendar.query(ancestor=user.key)\
                        .filter(ndb.AND(Calendar.owner==user.key,
                                        Calendar.name==calendar_name))
    calendars = cal_query.fetch()
    if len(calendars) == 0:
        raise DoesNotExistError('Calendar %s owned by %s does not exist',
                                calendar_name,
                                user.username)
    if len(calendars) > 1:
        raise Exception('This should never happen')
    return calendars[0]


def get_curr_user_from_email(email):
    email = email.lower()
    curr_user_query = User.query(ancestor=get_parent_key_for_email(email))\
                          .filter(User.email==email)
    curr_users = curr_user_query.fetch()
    if len(curr_users) == 0:
        create_user(email)
        return get_curr_user_from_email(email)
    elif len(curr_users) > 1:
        raise Exception('this should not happen')
    curr_user = curr_users[0]
    return curr_user


def get_curr_user_from_username(username):
    curr_user_query = User.query().filter(User.username==username)
    curr_users = curr_user_query.fetch()
    if len(curr_users) == 0:
        create_user(email)
        return get_curr_user_from_username(username)
    elif len(curr_users) > 1:
        raise Exception('this should not happen')
    curr_user = curr_users[0]
    return curr_user


def create_user(email):
    email = email.lower()
    username = username_re.match(email).group(1)
    user = User(parent=get_parent_key_for_email(email),
                username=username,
                email=email,
                calendars_following=[])
    user.put()
    return user


def user_exists(email):
    return not not User.query().filter(User.email==email).fetch()
