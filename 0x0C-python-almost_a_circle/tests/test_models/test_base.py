import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_create_instance(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_create_instance_with_id(self):
        b2 = Base(10)
        self.assertIsInstance(b2, Base)
        self.assertEqual(b2.id, 10)

    def test_create_multiple_instances(self):
        b3 = Base()
        b4 = Base()
        self.assertNotEqual(b3.id, b4.id)

if __name__ == '__main__':
    unittest.main()

