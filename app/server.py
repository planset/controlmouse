from __future__ import print_function
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.options import define
define("port", default=8000, help="run on the given port", type=int)
def get_ipaddr():
    import subprocess
    ipaddr = '127.0.0.1'
    lines = subprocess.check_output(['ifconfig | grep -E "inet\s" | cut -d" " -f2'], shell=True)
    for line in reversed(lines.split('\n')):
        if line == '127.0.0.1':
            break
        ipaddr = line
    return ipaddr
class Main(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",ipaddr=get_ipaddr())
class ControlMouseWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print('open')
    def on_message(self, message):
        x, y = message.split(',')
        print('move to ', x, ',', y)
        os.system('bin/PostMouseEvent {x} {y}'.format(x=x, y=y))

    def on_close(self):
        print('close')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r'/', Main),
                (r'/ws', ControlMouseWebSocket),
                ]
        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__), "templates"),
                debug=True,
                )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
