#!/usr/bin/env python2

import webapp2
from handlers.calendar_page_handler import CalendarPageHandler, GenerateDatesHandler
from handlers.dashboard_page_handler import DashboardPageHandler
from handlers.create_user_page_handler import CreateUserPageHandler

app = webapp2.WSGIApplication([
    (r'/', DashboardPageHandler),
    (r'/calendar/(.+?)/(.+?)[/]?', CalendarPageHandler),
    (r'/generate-calendar', GenerateDatesHandler),
], debug=True)
