"""MODULES"""
import json
import hashlib
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException




class TestOrderManager(TestCase):
    """Class representing the information required for TEST ORDER MANAGER"""
    @freeze_time("2023-02-19")
    def test_send_product_correct_t1(self):
        """TEST OKEY OF SEND PRODUCT"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test1_correct.json"
        my_order=OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        my_value = my_order.send_product(file)
        self.assertEqual("19c6f9850bee5e10f75770fd58afb9f79b4951794fec0055ea59c6eb15ac4620", my_value)
        store = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store\store_shipping.json"
        with open(store,"r", encoding = "utf-8") as file:
            data_list_file = json.load(file)
        found = False
        for i in data_list_file:
            if i["_OrderShipping__tracking_code"] == my_value:
                found = True
        self.assertTrue(found)

    def test_send_product_incorrect_t2_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T2DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test2_delete.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t2_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T2DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test2_duplicate.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t3_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T3DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test3_delete.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t3_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T3DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test3_duplicate.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)
