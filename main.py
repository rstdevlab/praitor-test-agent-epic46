"""Disposable test-agent "hello" service.

Stdlib-only single-endpoint HTTP service. This repo is disposable and
non-production -- see README.md.
"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8080


class HelloHandler(BaseHTTPRequestHandler):
    timeout = 10  # bound a slow/half-open client so one connection can't wedge the service

    def do_GET(self):
        if self.path.split("?", 1)[0] != "/":
            self.send_response(404)
            self.end_headers()
            return
        body = json.dumps({"message": "hello from praitor-test-agent-epic46"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_request(self, code="-", size="-"):
        pass  # keep stdout quiet for the access log; log_error stays intact for failures


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", PORT), HelloHandler).serve_forever()
