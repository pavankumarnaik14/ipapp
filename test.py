import unittest    
from urllib.request import urlopen
import json

class TestApp(unittest.TestCase):
    def test_remote_addr(self):
        hostname = json.load(urlopen('http://ipinfo.io/json'))
        self.assertRegex(hostname['ip'],r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')

if __name__ == '__main__':
    unittest.main()
