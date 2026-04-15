import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        # 8 spaces gap before self
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()