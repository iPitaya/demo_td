import tornado
import tornado.process
import tornado.web
from tornado import httpserver
from tornado import ioloop
from tornado.web import RequestHandler
class non(RequestHandler):
	def get(self):
		self.write("hello")
def main():
	"""docstring for main"""
	sokets = tornado.netutil.bind_sockets(8080)
	tornado.process.fork_processes(0)
	application = tornado.web.Application([(r'/',non)],)
	http_server = httpserver.HTTPServer(application)
	http_server.add_sockets(sokets)
	ioloop.IOLoop.instance().start()

if __name__ == '__main__':
	main()
