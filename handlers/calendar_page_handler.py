
from base_handler import BaseHandler


class CalendarPageHandler(BaseHandler):


    template_name = 'calendar-page/calendar-page.html'


    def get_template(self):
        return self.get_template_by_name(CalendarPageHandler.template_name)


    def add_values(self, values):
        pass
