# demo_td
tornado dem

tornado 开发入门
1.安装 tornado开发环境
2.基本框架

# -*- coding:utf-8 -*-
import os
import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define,options

settings = {
    "debug":True,
    "static_patch":os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url":"/login"
}

urls = [
    (r"/home",HomeHandler),
    ]

application = tornado.web.Application(urls,**settings)
define('port',default = 12306,help='tornado\'s port',type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application,xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

3.并发 协程：
方法1：
class Test(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		yield self.callback()
	
	@tornado.gen.coroutine
	def callback(self):
		raise tornado.gen.Return()

方法2：
class Test(tornado.web.RequestHandler):
	executor = ThreadPoolExecutor(4)
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self):
		yield self.callback()
		self.finish()

	@run_on_executor
	def callback(self):
		return 
