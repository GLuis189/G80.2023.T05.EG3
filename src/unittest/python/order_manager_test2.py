from unittest import TestCase
from freezegun import freeze_time
import json
import hashlib
from pathlib import Path
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_send_product_correct_t1(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = JSON_STORE_PATH + "test1_correct.json"
        my_order=OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        my_value = my_order.send_product(file)
        self.assertEqual("19c6f9850bee5e10f75770fd58afb9f79b4951794fec0055ea59c6eb15ac4620", my_value)
        store = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\store\store_shipping.json"
        with open(store,"r", encoding = "utf-8") as file:
            data_list_file = json.load(file)
        found = False
        for i in data_list_file:
            if i["_OrderShipping__tracking_code"] == my_value:
                found = True
        self.assertTrue(found)

    def test_send_product_incorrect_t2_delete(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = JSON_STORE_PATH + "test2_delete.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash_original = hashlib.md5(file.__str__().encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash = hashlib.md5(file.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash)

    def test_send_product_incorrect_t2_duplicate(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = JSON_STORE_PATH + "test2_duplicate.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash_original = hashlib.md5(file.__str__().encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash = hashlib.md5(file.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash)

    def test_send_product_incorrect_t3_delete(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = JSON_STORE_PATH + "test3_delete.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash_original = hashlib.md5(file.__str__().encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash = hashlib.md5(file.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash)

    def test_send_product_incorrect_t3_duplicate(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = JSON_STORE_PATH + "test3_duplicate.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash_original = hashlib.md5(file.__str__().encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_value = my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            hash = hashlib.md5(file.__str__().encode()).hexdigest()
        self.assertEqual(hash_original, hash)

