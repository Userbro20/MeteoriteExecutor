from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.translate_path(self.path)
        if not os.path.exists(path):
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            with open('404.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            super().do_GET()

TCPServer(('', 5500), CustomHandler).serve_forever()