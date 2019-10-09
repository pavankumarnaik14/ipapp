import unittest
import socket    
from urllib.request import urlopen
import json
def index():
    return str(request.remote_addr)
class TestApp(unittest.TestCase):
    def test_remote_addr(self):
        hostname = json.load(urlopen('http://ipinfo.io/json'))
        self.assertEqual('157.45.49.149',hostname['ip'])

if __name__ == '__main__':
    unittest.main()