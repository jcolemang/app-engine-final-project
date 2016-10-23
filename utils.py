from google.appengine.ext import ndb
import re

from models import User, Calendar


username_re = re.compile('(.*)@.*')


def get_parent_key_for_email(email):
    return ndb.Key("Entity", email.lower())


def put_calendar_for_user(email, calendar_name):
    user = get_curr_user_from_email(email)
    calendar = Calendar(parent=user.key,
                        name=calendar_name)
    calendar.put()
    return calendar


def query_user_calendars(email):
    user = get_curr_user_from_email(email)
    calendar_query = Calendar.query(ancestor=user.key)
    return calendar_query


def get_curr_user_from_email(email):
    email = email.lower()
    curr_user_query = User.query().filter(User.email==email)
    curr_users = curr_user_query.fetch()
    if len(curr_users) != 1:
        return False
    curr_user = curr_users[0]
    return curr_user


def create_user(email):
    email = email.lower()
    username = username_re.match(email).group(1)
    user = User(username=username,
                email=email,
                calendars_following=[])
    user.put()
    return user


def user_exists(email):
    return not not User.query().filter(User.email==email).fetch()
