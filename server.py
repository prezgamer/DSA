import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from DataParser import ParseToAdjList, create_airport_bst, getCoordinates
from main import main


class RequestHandler(BaseHTTPRequestHandler):
    
    print("Setting up server...")
    
    # create adjacency list of flight routes
    adjListGraph = ParseToAdjList()
    # create list of all airport's coordinates for A*star algorithm
    # coordinates = getCoordinates()ss
    # create binary search tree of airport objects
    airportsBST = create_airport_bst()
    
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    
    def do_GET(self):
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        try:
            results = main(params['param1'][0], params['param2'][0], self.airportsBST, self.adjListGraph, self.cost)
        except KeyError:
            print("No route exists for given airports")
            results = None
        except:
            print("Invalid airport names given")
            results = None

        self._set_headers()
        self.wfile.write(bytes(json.dumps(results), "utf8"))
        return


def run():
    # set up http server
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server up and running...')
    httpd.serve_forever()
 

run()