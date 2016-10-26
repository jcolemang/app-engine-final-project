from google.appengine.ext import ndb


class DoesNotExistError(Exception):
    pass


class SpecialText(ndb.Model):
    text = ndb.StringProperty()
    date = ndb.DateProperty()
    tag = ndb.StringProperty()


class Cell(ndb.Model):
    text = ndb.StringProperty()
    row_num = ndb.IntegerProperty()


class Calendar(ndb.Model):

    default_columns = ['session', 'content', 'due', 'preparation']

    owner = ndb.KeyProperty()
    name = ndb.StringProperty()
    date_created = ndb.DateProperty(auto_now=True)
    column_names = ndb.StringProperty(repeated=True)
    cells = ndb.KeyProperty(kind=Cell, repeated=True)


class User(ndb.Model):
    username = ndb.StringProperty()
    email = ndb.StringProperty()
    calendars_following = ndb.KeyProperty(kind=Calendar,
                                          repeated=True)
