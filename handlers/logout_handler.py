from handlers.base_handler import BaseHandler


class LogoutHandler(BaseHandler):
    def get(self):
        del self.session["user_info"]
        self.redirect(uri="/blank")