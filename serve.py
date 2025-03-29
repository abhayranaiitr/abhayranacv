from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = 8001
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT} from {DIRECTORY}")
    httpd.serve_forever()