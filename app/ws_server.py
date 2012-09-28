from __future__ import print_function
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

from tornado.options import define

define("port", default=8000, help="run on the given port", type=int)


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
                (r"/move", ControlMouseWebSocket),
                ]
        settings = dict(
                debug=True,
                )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
    
