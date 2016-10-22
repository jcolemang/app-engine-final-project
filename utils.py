from google.appengine.ext import ndb

from models import User


def get_parent_key_for_email(email):
    """ Gets the parent key (the key that is the parent to all Datastore data for this user) from the user's email. """
    return ndb.Key("Entity", email.lower())
  
  
def get_curr_user_from_email(email):
  
    email = email.lower()
    curr_user = User.get_by_id(email,parent=get_parent_key_for_email(email))
# TODO: change username to redirect later
    if not curr_user:
      curr_user = User(email=email, username=email, calendars_following=[],parent=get_parent_key_for_email(email)) 
      curr_user.put()
      
    return curr_user
    