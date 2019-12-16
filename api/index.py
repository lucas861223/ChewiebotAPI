from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        username = parse_qs(urlparse(self.path).query)['username'][0]
        response = requests.get(url="https://api.twitch.tv/helix/users?login=" + username,
                                headers={"client-id": "w07tun6ja438fsymn61ei88tm8kw7q"})
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.json()['data'][0]['id'].encode())
        return