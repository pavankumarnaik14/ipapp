import unittest
import socket    
from urllib.request import urlopen
import json
def index():
    return str(request.remote_addr)
class TestApp(unittest.TestCase):
    def test_remote_addr(self):
        hostname = json.load(urlopen('http://ipinfo.io/json'))
        self.assertRegex(hostname['ip'],r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

if __name__ == '__main__':
    unittest.main()