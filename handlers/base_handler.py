
from webapp2 import RequestHandler
import os
from jinja2 import Environment, FileSystemLoader

class BaseHandler(RequestHandler):

    # setting the environment
    template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
    env = Environment(loader=FileSystemLoader([template_path]))
    template_name = None

    def get(self):
        template = self.get_template()
        values = self.get_base_values()
        self.add_values(values)
        self.response.write(template.render(values))


    def get_template_by_name(self, template_name):
        return self.get_env().get_template(template_name)


    def get_template(self):
        raise RuntimeError('Must override get_template')


    def get_base_values(self):
        return {
            'path': self.request.path,
        }


    def add_values(self, values):
        pass


    def get_env(self):
        return BaseHandler.env
