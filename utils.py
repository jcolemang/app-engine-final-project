from google.appengine.ext import ndb

from models import User, Calendar



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
        curr_user = User(parent=get_parent_key_for_email(email),
                         email=email,
                         username=email,
                         calendars_following=[])
        curr_user.put()
    else:
        curr_user = curr_users[0]
    return curr_user
