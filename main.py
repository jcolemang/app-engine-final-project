#!/usr/bin/env python2

import webapp2
from handlers.base_handler import BaseHandler
from handlers.calendar_page_handler import CalendarPageHandler
from handlers.dashboard_page_handler import DashboardPageHandler

app = webapp2.WSGIApplication([
    ('/', DashboardPageHandler),
    ('/calendar', CalendarPageHandler),
], debug=True)
