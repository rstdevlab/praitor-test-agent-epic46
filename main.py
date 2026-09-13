"""Disposable test-agent "hello" service.

Stdlib-only single-endpoint HTTP service. This repo is disposable and
non-production -- see README.md.
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/":
            self.send_response(404)
            self.end_headers()
            return
        body = json.dumps({"message": "hello from praitor-test-agent"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass  # keep stdout quiet; not needed for a disposable demo service


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", PORT), HelloHandler).serve_forever()
