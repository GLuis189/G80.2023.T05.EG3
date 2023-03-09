from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException


class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_register_order_okey(self):
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="calle colmenarejo",
                                            zip_code="28345", phone="123456789", order_type="premium")
        self.assertEqual("a5d8a05c1d4c9dfd9eb8bf48d23cd804", my_value)
    def test_with_product_code_wrong_character(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("84216914222A", "C/LISBOA,4, MADRID, SPAIN", "PREMIUM", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    def test_with_product_code_wrong_sum(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423225", "C/LISBOA,4, MADRID, SPAIN", "PREMIUM", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    def test_with_product_code_wrong_length_less(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322", "C/LISBOA,4, MADRID, SPAIN", "PREMIUM", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    def test_with_product_code_wrong_length_more(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("84216914232200", "C/LISBOA,4, MADRID, SPAIN", "PREMIUM", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)

    def test_with_order_type_okey(self):
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="calle colmenarejo",
                                           zip_code="28345", phone="123456789", order_type="PREMIUM")
        self.assertEqual(my_value., "PREMIUM")
