"""Self-check variant: speculative multi-user web service added for a hypothetical future."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Notes(BaseHTTPRequestHandler):
    def do_GET(self):
        body = open('notes.json', 'rb').read()
        self.send_response(200); self.end_headers(); self.wfile.write(body)

if __name__ == '__main__':
    HTTPServer(('127.0.0.1', 8080), Notes).serve_forever()
