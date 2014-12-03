# -*- coding: utf-8 -*-

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from session import Session
from redis import client

class MainHandler(RequestHandler):
    def initialize(self):
        self.redis = self.application.redis
        
    def get(self):
        if not self.get_secure_cookie("sessionid"): # 带签名的 cookie用get_secure_cookie获取
            self.set_secure_cookie("sessionid", "112358", 1) # 带签名的 cookie用set_secure_cookie设置, 1天过期
            self.write("U r cookie is not yet!")
        else:
            self.write("U r cookie is %s." % self.get_secure_cookie("sessionid"))
        session = self.application.session(self)
        if self.application.test_flag == 0:
            session.fk = "flyking"
            self.application.test_flag = 1
        print session.fk

urls = [
        (r"/", MainHandler),

    ]
settings = {
        "cookie_secret":"61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=", # 带签名的cookie
        "xsrf_cookies":"Ture", # 跨站伪造请求(Cross-site request forgery) 防范策略 xsrf_cookies
        
    }

app = Application(urls, **settings)
app.listen(8888)
app.redis = client.Redis()
app.session = Session
app.test_flag = 0

IOLoop.instance().start()
