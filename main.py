#!/usr/bin/env python2

import webapp2
from handlers.base_handler import BaseHandler
from handlers.calendar_page_handler import CalendarPageHandler

app = webapp2.WSGIApplication([
    ('/', BaseHandler),
    ('/calendar', CalendarPageHandler),
], debug=True)
