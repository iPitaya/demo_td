import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.autoreload
import tornado.process
import tornado.netutil

class MainHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		self.write("Hello,world")
		self.finish()

application = tornado.web.Application([
	(r"/",MainHandler),
])

if __name__ == "__main__":
	#sockes = tornado.netutil.bind_sockets(8080)
	#tornado.process.fork_processes(0)
	http_server = tornado.httpserver.HTTPServer(application)
	application.listen(8888)
	#http_sever.add_sockets(sockes)
	loop = tornado.ioloop.IOLoop.instance()
	tornado.autoreload.start(loop)
	loop.start()

