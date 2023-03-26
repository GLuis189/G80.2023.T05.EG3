import json
import hashlib
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def crear_my_order_premium(self):
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test1_correct.json"
        return my_order.send_product(file)

    @freeze_time("2023-02-19")
    def crear_my_order_regular(self):
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="REGULAR")
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test1_correct_r.json"
        return my_order.send_product(file)
    @freeze_time("2023-02-26")
    def test_deliver_product_regular(self):
        my_order = OrderManager()
        delivery = my_order.deliver_product(self.crear_my_order_regular())
        self.assertTrue(delivery)

    @freeze_time("2023-02-20")
    def test_deliver_product_premium(self):
        my_order = OrderManager()
        delivery = my_order.deliver_product(self.crear_my_order_premium())
        self.assertTrue(delivery)
