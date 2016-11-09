#!/usr/bin/env python2

import webapp2

from handlers.blank_handler import BlankHandler
from handlers.calendar_page_handler import CalendarPageHandler, GenerateDatesHandler
from handlers.dashboard_page_handler import DashboardPageHandler
from handlers.login_handler import LoginHandler
from handlers.logout_handler import LogoutHandler


config = {}
config["webapp2_extras.sessions"] = {
    'secret_key': 'Pho4xZW6cOebVlK0hcDQ'
    }
    
app = webapp2.WSGIApplication([
    (r'/', DashboardPageHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/blank', BlankHandler),
    (r'/calendar/(.+?)/(.+?)[/]?', CalendarPageHandler),
    (r'/generate-calendar', GenerateDatesHandler),
], config=config, debug=True)
