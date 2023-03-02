from unittest import TestCase
from uc3m_logistics import OrderManager

class TestOrderManager(TestCase):
    def test_register_order_okey(self):
        my_order = OrderManager()
        my_value =  my_order.register_order(product_id="3662168005326", address="calle colmenarejo",
                                            zip_code="28345", phone="123456789", order_type="premium")
        self.assertEqual(my_value, "caca")

