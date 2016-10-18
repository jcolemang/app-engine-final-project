from google.appengine.ext import ndb
from google.appengine.api.validation import Repeated

class User(ndb.Model):
  username = ndb.StringProperty()
  email = ndb.StringProperty()
  calendars_following = ndb.KeyProperty(Repeated)
  
class Calendar(ndb.Model):
  owner = ndb.KeyProperty()
  header = ndb.StringProperty()
  date_created = ndb.DateProperty()
  
class Cell(ndb.Model):
  text = ndb.StringProperty(Repeated)
  SpecialText = ndb.StructuredProperty(Repeated)
  
class SpecialText(ndb.Model):
  text = ndb.StringProperty()
  date = ndb.DateProperty()
  tag = ndb.StringProperty()
  
    
