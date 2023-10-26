import http.server
import socketserver
import urllib.parse
import random
import string
# Dictionary to store short codes and their corresponding URLs
url_store = {}

class ShortenHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Welcome to the URL Shortener. To shorten a URL, use POST request.')
        elif parsed_path.path in url_store:
            self.send_response(301)
            self.send_header('Location', url_store[parsed_path.path])
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Short URL not found.')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        long_url = post_data.decode('utf-8')

        short_code = generate_short_code()
        url_store[short_code] = long_url

        response = f'Short URL: {self.server.server_address[0]}:{self.server.server_address[1]}/{short_code}'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

def run(server_class=http.server.HTTPServer, handler_class=ShortenHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting URL Shortener on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
