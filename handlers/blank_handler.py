from handlers.base_handler import BaseHandler

class BlankHandler(BaseHandler):
    template_name = '/login.html'
    
    def get_template(self):
        return self.get_template_by_name(BlankHandler.template_name)
    
    def get(self):
        template = self.get_template()
        self.response.write(template.render())
      