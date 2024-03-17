import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from main import main

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        # self.send_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
        self.end_headers()
    
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        # print(params)  # Prints the parameters to the console
        try:
            results = main(params['param1'][0], params['param2'][0])
        except KeyError:
            print("No route exists for given airports")
            results = None
        except:
            print("Invalid airport names given")
            results = None
        # message = (params['param1'][0], params['param2'][0])
        self._set_headers()
        self.wfile.write(bytes(json.dumps(results), "utf8"))
        return

def run():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Running server...')
    httpd.serve_forever()

run()