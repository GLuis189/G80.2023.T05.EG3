from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException


class TestOrderManager(TestCase):

    def test_with_product_code_wrong(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322A","PREMIUM","C/LISBOA,4, MADRID, SPAIN", "+34123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    @freeze_time("2023-02-19")
    def test_register_order_okey(self):
        my_order = OrderManager()
        my_value =  my_order.register_order(product_id="3662168005326", adress="calle colmenarejo",
                                            zip_code="28345", phone="123456789", order_type="premium")
        self.assertEqual("ca7b53b6cea20d37e29164243944bcc0", my_value)