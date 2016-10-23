from google.appengine.ext import ndb


class Calendar(ndb.Model):
  owner = ndb.KeyProperty()
  name = ndb.StringProperty()
  date_created = ndb.DateProperty()

class User(ndb.Model):
  username = ndb.StringProperty()
  email = ndb.StringProperty()
  calendars_following = ndb.KeyProperty(kind=Calendar,
                                        repeated=True)

class SpecialText(ndb.Model):
  text = ndb.StringProperty()
  date = ndb.DateProperty()
  tag = ndb.StringProperty()

class Cell(ndb.Model):
  text = ndb.StringProperty(repeated=True)
  special_text = ndb.StructuredProperty(SpecialText,
                                       repeated=True)
