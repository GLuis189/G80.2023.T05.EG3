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

    def test_send_product_incorrect_vacio(self):
        """TEST NOT OKEY OF SEND PRODUCT TEST_PRODUCT_EMTY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test_vacio.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t2_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T2DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test2_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t2_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T2DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test2_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t3_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T3DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test3_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t3_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T3DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test3_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t4_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T3DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test4_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t4_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T4DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test4_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t5_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T5MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test5_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t6_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T6DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test6_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t6_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T6DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test6_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t7_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T7DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test7_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t7_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T7DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test7_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t8_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T8DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test8_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t8_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T8DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test8_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t9_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T9MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test9_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t10_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T10DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test10_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t10_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T10DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test10_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t11_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T11DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test11_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t11_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T11DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test11_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t12_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T12DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test12_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t12_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T12DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test12_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t13_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T13MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test13_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t14_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T14DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test14_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t14_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T14DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test14_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t15_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T15DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test15_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t15_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T15DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test15_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t16_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T16DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test16_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t16_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T16DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test16_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t17_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T17DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test17_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t17_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T17DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test17_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t18_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T18DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test18_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid key", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t18_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T18DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test18_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid key", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t19_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T19DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test19_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t19_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T19DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test19_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t20_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T20MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test20_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)


    def test_send_product_incorrect_t21_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T21DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test21_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t21_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T21DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test21_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t22_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T22DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test22_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid hash", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t22_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T22DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test22_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid hash", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t23_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T23DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test23_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t23_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T23DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test23_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t24_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T24DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test23_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t24_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T24DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test23_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t25_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T25DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test25_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid key", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t25_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T25DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test25_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid key", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t26_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T26DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test26_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t26_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T26DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test26_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t27_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T27MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test27_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t28_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T28DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test28_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t28_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T28DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test28_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t29_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T29DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test29_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t29_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T29DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test29_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t30_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T30DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test30_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t30_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T30DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test30_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t31_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T31MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test31_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t32_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T32MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test32_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid key", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t33_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T33MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test33_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t34_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T34MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test34_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t35_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T35DMODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test35_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid hash", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t36_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T36MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test36_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t37_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T37MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test37_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t38_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T38MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test38_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid key", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t39_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T39MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test39_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t40_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T40MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test40_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)


    def test_send_product_incorrect_t41_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T41DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test41_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    @freeze_time("2023-02-19")
    def test_send_product_correct_t41_duplicate(self):
        """TEST OKEY OF SEND PRODUCT T41_DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test41_duplicate.json"
        my_order = OrderManager()
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

    def test_send_product_incorrect_t42_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T42DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test42_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t42_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T42DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test42_duplicate.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t43_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T43DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test43_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    @freeze_time("2023-02-19")
    def test_send_product_correct_t43_duplicate(self):
        """TEST OKEY OF SEND PRODUCT T43_DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test43_duplicate.json"
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        my_value = my_order.send_product(file)
        self.assertEqual("19c6f9850bee5e10f75770fd58afb9f79b4951794fec0055ea59c6eb15ac4620", my_value)
        store = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store\store_shipping.json"
        with open(store, "r", encoding="utf-8") as file:
            data_list_file = json.load(file)
        found = False
        for i in data_list_file:
            if i["_OrderShipping__tracking_code"] == my_value:
                found = True
        self.assertTrue(found)

    def test_send_product_incorrect_t44_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T44DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test44_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t44_duplicate(self):
        """TEST NOT OKEY OF SEND PRODUCT T44DUPLICATE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test44_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t45_delete(self):
        """TEST NOT OKEY OF SEND PRODUCT T45DELETE"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test45_delete.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t46_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T46MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test46_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    @freeze_time("2023-02-19")
    def test_send_product_correct_t47_modify(self):
        """TEST OKEY OF SEND PRODUCT T47_MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test47_modify.json"
        my_order = OrderManager()
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



    def test_send_product_incorrect_t48_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T48MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test48_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    @freeze_time("2023-02-19")
    def test_send_product_correct_t49_modify(self):
        """TEST OKEY OF SEND PRODUCT T49_MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test49_modify.json"
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        my_value = my_order.send_product(file)
        self.assertEqual("19c6f9850bee5e10f75770fd58afb9f79b4951794fec0055ea59c6eb15ac4620", my_value)
        store = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store\store_shipping.json"
        with open(store, "r", encoding="utf-8") as file:
            data_list_file = json.load(file)
        found = False
        for i in data_list_file:
            if i["_OrderShipping__tracking_code"] == my_value:
                found = True
        self.assertTrue(found)

    def test_send_product_incorrect_t50_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T50MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test50_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_t51_modify(self):
        """TEST NOT OKEY OF SEND PRODUCT T51MODIFY"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test51_modify.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_hash_short(self):
        """TEST NOT OKEY SHORT HASH"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test_hash_short.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid hash", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_hash_long(self):
        """TEST NOT OKEY LONG HASH"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test_hash_long.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid hash", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_hash_character(self):
        """TEST NOT OKEY INCORRECT CHARACTER HASH"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test_hash_character.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid hash", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)

    def test_send_product_incorrect_email_long(self):
        """TEST NOT OKEY LONG EMAIL"""
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file_send = json_store_path + "test_email_long.json"
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_store_path + "store_shipping.json"
        with open(file_send, "r", encoding="utf-8", newline="") as file:
            file = str(file)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_original = hashlib.md5(file.encode()).hexdigest()
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        with self.assertRaises(OrderManagementException) as cm:
            my_order.send_product(file_send)
        self.assertEqual("Invalid email", cm.exception.message)
        with open(file_store, "r", encoding="utf-8", newline="") as file:
            file = str(file)
            hash_lib = hashlib.md5(file.encode()).hexdigest()
        self.assertEqual(hash_original, hash_lib)
