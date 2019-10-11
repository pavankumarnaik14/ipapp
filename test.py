import unittest    
from urllib.request import urlopen
import json

class TestApp(unittest.TestCase):
    def test_remote_addr(self):
        hostname = json.load(urlopen('http://ipinfo.io/json'))
        self.assertRegex(hostname['ip'],r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

if __name__ == '__main__':
    unittest.main()
