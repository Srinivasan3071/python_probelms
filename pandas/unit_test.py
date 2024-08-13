import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 4)
        self.assertEqual(add(-1, 1), 1)

# Directly call unittest.main() to run the tests
unittest.main()
