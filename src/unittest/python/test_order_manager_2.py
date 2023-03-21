from unittest import TestCase
from uc3m_logistics import OrderManager

class TestOrderManager(TestCase):
    def test_send_product(self):
        my_order=OrderManager()
        my_value = my_order.send_product("track.json")
        return my_value
