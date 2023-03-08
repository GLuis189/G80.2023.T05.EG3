"""class for testing the regsiter_order method"""
import unittest
from uc3m_logistics import OrderManager

class MyTestCase(unittest.TestCase):
    """class for testing the register_order method"""
    def test_1( self ):
        """dummy test"""
        self.assertEqual(True, OrderManager.validate_ean13(self.product_id))


if __name__ == '__main__':
    unittest.main()
