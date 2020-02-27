import unittest
from Task5 import url
class TestMyProgram (unittest.TestCase):
    def test_list_int(self):
        self.assertEqual(url, 'http://172.17.50.43/freebix')
if __name__ == '__main__':
    unittest.main ()