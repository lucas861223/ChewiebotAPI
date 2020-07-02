from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        username = parse_qs(urlparse(self.path).query)['username'][0]
        response = requests.get(url="https://api.twitch.tv/kraken/users?login=" + "lucas861223",
                                headers={"client-id": "xnpbm69um56zzge4yh6ojhg1rg23s1",
                                         "Accept": "application/vnd.twitchtv.v5+json"})
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.json()['users'][0]['_id'].encode())
        return