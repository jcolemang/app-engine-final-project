#!/usr/bin/env python2

import webapp2
from handlers.base_handler import BaseHandler

app = webapp2.WSGIApplication([
    ('/', BaseHandler)
], debug=True)
