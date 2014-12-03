# -*- coding:utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define,options
from mainhandler  import MainHandler

settings = {
    "debug":True,
    "static_patch":os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url":"/login"
}

urls = [
    (r"/home",MainHandler),
    ]

application = tornado.web.Application(urls,**settings)
define('port',default = 12300,help='tornado\'s port',type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application,xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
