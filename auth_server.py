from http.server import BaseHTTPRequestHandler, HTTPServer

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handle_auth()

    def do_POST(self):
        self.handle_auth()

    def handle_auth(self):
        username = self.headers.get("Auth-User")
        password = self.headers.get("Auth-Pass")

        print("Auth attempt:", username, password)
        self.send_response(200)

        if username == "test" and password == "password" :
            self.send_header("Auth-Status", "OK")
            self.send_header("Auth-Server", "127.0.0.1")
            self.send_header("Auth-Port", "2525")
        else:
            self.send_header("Auth-Status", "Invalid login")
            self.send_header("Auth-Wait", "3")

        self.end_headers()

if __name__ == "__main__":
    print("Auth server running on port 9123...")
    HTTPServer(("127.0.0.1", 9123), AuthHandler).serve_forever()
