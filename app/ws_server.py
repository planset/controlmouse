import os
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

content = ''

def app(environ, start_response):
    if environ["PATH_INFO"] == '/move':
        ws = environ["wsgi.websocket"]
        while True:
            src = ws.receive()
            print 'src:', src
            if src is None:
                break
            x, y = src.split(',')
            print x, '', y
            os.system('bin/PostMouseEvent {x} {y}'.format(x=x, y=y))
    else:
        start_response("200 OK", [
                ("Content-Type", "text/html"),
                ("Content-Length", str(len(content)))
                ])  
        return iter([content])

if __name__=="__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 8000), app, handler_class=WebSocketHandler)
    server.serve_forever()


