
from webapp2 import RequestHandler
import os
from jinja2 import Environment, FileSystemLoader

class BaseHandler(RequestHandler):

    # setting the environment
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    env = Environment(loader=FileSystemLoader([template_path]))


    def get(self):
        template = self.get_template()
        self.response.write(template.render())


    def get_template(self):
        return self.get_env().get_template('base-page.html')


    def get_env(self):
        return BaseHandler.env
