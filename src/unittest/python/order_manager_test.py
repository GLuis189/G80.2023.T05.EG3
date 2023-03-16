import json
import os
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException


class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_register_order_okey_premium(self):
        """if os.path.isfile(file_store):
            os.remove(file_store)"""
        #COMPROBACIÓN DEL HASH
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                            zip_code="28345", phone="123456789", order_type="PREMIUM")
        self.assertEqual("f72071fad57d01cd121d6dde86ae3fa5", my_value)
        #COMPROBACIÓN DE QUE LO GUARDA EN EL ALMACÉN
        JSON_FILES_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = JSON_FILES_PATH + "store_request.json"
        with (open(file_store,"r", encoding= "UTF-8", newline="")) as file:
            data_list= json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == my_value:
                found = True
        if found == False:
            data_list.append(my_order.__dict__)
        self.assertTrue(found)

    @freeze_time("2023-02-19")
    def test_register_order_okey_regular(self):
        """if os.path.isfile(file_store):
            os.remove(file_store)"""
        # COMPROBACIÓN DEL HASH
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                           zip_code="28345", phone="123456789", order_type="REGULAR")
        self.assertEqual("2cce00815ff818105d168f74bc8ddcd3", my_value)
        # COMPROBACIÓN DE QUE LO GUARDA EN EL ALMACÉN
        JSON_FILES_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = JSON_FILES_PATH + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == my_value:
                found = True
        if found == False:
            data_list.append(my_order.__dict__)
        self.assertTrue(found)

    def test_with_product_code_wrong_character(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("84216914222A","PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    def test_with_product_code_wrong_sum(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    def test_with_product_code_wrong_length_less(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
    def test_with_product_code_wrong_length_more(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("84216914232200", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)

    def test_with_order_type_invalid(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322", "PRE", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid Order Type", cm.exception.message)

    def test_with_address_wrong_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRIDD", "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)

    def test_with_address_wrong_long(self):
        string = "a" * 101
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("3662168005326", "PREMIUM", string, "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)

    def test_with_address_wrong_spaces(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4,MADRID,SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)

    def test_with_phone_wrong_character(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "12345678A",
                                            "28005")
        self.assertEqual("Invalid Phone", cm.exception.message)

    def test_with_phone_wrong_length_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "12345678",
                                            "28005")
        self.assertEqual("Invalid Phone", cm.exception.message)

    def test_with_phone_wrong_length_more(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("3662168005326", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "1234567899",
                                            "28005")
        self.assertEqual("Invalid Phone", cm.exception.message)

    def test_with_zip_code_character(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "2800A")
        self.assertEqual("Invalid Zip Code", cm.exception.message)

    def test_with_zip_code_length_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "2800")
        self.assertEqual("Invalid Zip Code", cm.exception.message)

    def test_with_zip_code_length_more(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("3662168005326", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "280055")
        self.assertEqual("Invalid Zip Code", cm.exception.message)