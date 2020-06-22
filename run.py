from endpoints import app
import gevent
from gevent.wsgi import WSGIServer

http_server = WSGIServer(('', 8080), app)
http_server.serve_forever()

