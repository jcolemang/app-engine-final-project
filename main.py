#!/usr/bin/env python2

import webapp2
import os
from jinja2 import Environment, FileSystemLoader

# will likely need to replace this later
template_path = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = Environment(loader=FileSystemLoader([template_path]))


class BaseHandler(webapp2.RequestHandler):

    def get(self):
        template = self.get_template()
        self.response.write(template.render())

    def get_template(self):
        return jinja_env.get_template('base-page.html')




app = webapp2.WSGIApplication([
    ('/', BaseHandler)
])
