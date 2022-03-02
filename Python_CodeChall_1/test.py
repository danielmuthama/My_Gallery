from json.tool import main
import unittest
from demo import Reverse_Int

class reverseTest(unittest.TestCase):
    def test_reverse(self):
        
        self.assertEqual(Reverse_Int.reverse(789), 987)
        self.assertEqual(Reverse_Int.reverse(-789), -989)

if __name__ == '__main__':
    unittest.main()