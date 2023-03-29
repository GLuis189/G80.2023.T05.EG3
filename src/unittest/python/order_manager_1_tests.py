"""Module """
import json
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException


class TestOrderManager(TestCase):
    """Class for tests Order Manager"""
    @freeze_time("2023-02-19")
    def test_register_order_okey_premium(self):
        """Test okey PREMIUM"""
        #COMPROBACIÓN DEL HASH
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                            zip_code="28345", phone="123456789", order_type="PREMIUM")
        self.assertEqual("f72071fad57d01cd121d6dde86ae3fa5", my_value)
        #COMPROBACIÓN DE QUE LO GUARDA EN EL ALMACÉN
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store,"r", encoding= "UTF-8", newline="")) as file:
            data_list= json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == my_value:
                found = True
        if not found:
            data_list.append(my_order.__dict__)
        self.assertTrue(found)

    @freeze_time("2023-02-19")
    def test_register_order_okey_regular(self):
        """Test okey REGULAR"""
        # COMPROBACIÓN DEL HASH
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                           zip_code="28345", phone="123456789", order_type="REGULAR")
        self.assertEqual("2cce00815ff818105d168f74bc8ddcd3", my_value)
        # COMPROBACIÓN DE QUE LO GUARDA EN EL ALMACÉN
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == my_value:
                found = True
        if not found:
            data_list.append(my_order.__dict__)
        self.assertTrue(found)

    def test_with_product_code_wrong_character(self):
        """TEST WRONG PRODUCT_CODE """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("84216914222A","PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__product_id"] == "84216914222A":
                found = True
        self.assertFalse(found)

    def test_with_product_code_wrong_sum(self):
        """TEST WRONG PRODUCT_CODE """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423225", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__product_id"] == "8421691423225":
                found = True
        self.assertFalse(found)
    def test_with_product_code_wrong_length_less(self):
        """TEST WRONG PRODUCT_CODE """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("842169142322", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__product_id"] == "8421691423225":
                found = True
        self.assertFalse(found)

    def test_with_product_code_wrong_length_more(self):
        """TEST WRONG PRODUCT_CODE """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("84216914232200", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid EAN13 code string", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__product_id"] == "8421691423225":
                found = True
        self.assertFalse(found)

    def test_with_order_type_invalid(self):
        """TEST WRONG ORDER_TYPE """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("3662168005326", "PRE", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid Order Type", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_type"] == "PRE":
                found = True
        self.assertFalse(found)

    def test_with_address_wrong_short(self):
        """TEST WRONG ADDRESS """
        string = "a" * 18 + " "
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "PREMIUM", string, "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__delivery_address"] == string:
                found = True
        self.assertFalse(found)

    @freeze_time("2023-02-19")
    def test_with_address_correct_long21(self):
        """TEST ADDRESS LENGTH 21 """
        string = "a" * 10 + " " + "a" * 10
        # COMPROBACIÓN VALOR LIMITE 21
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address=string,
                                           zip_code="28345", phone="123456789", order_type="REGULAR")
        self.assertEqual("0cb76404d82d0984ccf67027d7a8b1ae", my_value)
        # COMPROBACIÓN DE QUE LO GUARDA EN EL ALMACÉN
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == my_value:
                found = True
        if not found:
            data_list.append(my_order.__dict__)
        self.assertTrue(found)

    def test_with_address_wrong_long(self):
        """TEST WRONG ADDRESS """
        string = "a" * 50 + " " + "a" * 50
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("3662168005326", "PREMIUM", string, "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__delivery_address"] == string:
                found = True
        self.assertFalse(found)

    @freeze_time("2023-02-19")
    def test_with_address_correct_long99(self):
        """TEST ADDRESS LENGTH 99 """
        string = "a" * 49 + " " + "a" * 49
        # COMPROBACIÓN VALOR LIMITE 99
        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address=string,
                                           zip_code="28345", phone="123456789", order_type="REGULAR")
        self.assertEqual("75d2107e967f0e8fbb2637084d9c0807", my_value)
        # COMPROBACIÓN DE QUE LO GUARDA EN EL ALMACÉN
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == my_value:
                found = True
        if not found:
            data_list.append(my_order.__dict__)
        self.assertTrue(found)

    def test_with_address_wrong_spaces(self):
        """TEST WRONG ADDRESS """
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4,MADRID,SPAIN", "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__delivery_address"] == "C/LISBOA,4,MADRID,SPAIN":
                found = True
        self.assertFalse(found)

    def test_with_phone_wrong_character(self):
        """TEST WRONG PHONE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "12345678A",
                                            "28005")
        self.assertEqual("Invalid Phone", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__phone_number"] == "12345678A":
                found = True
        self.assertFalse(found)

    def test_with_phone_wrong_length_short(self):
        """TEST WRONG PHONE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "12345678",
                                            "28005")
        self.assertEqual("Invalid Phone", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__phone_number"] == "12345678":
                found = True
        self.assertFalse(found)

    def test_with_phone_wrong_length_more(self):
        """TEST WRONG PHONE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("3662168005326", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "1234567899",
                                            "28005")
        self.assertEqual("Invalid Phone", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__product_id"] == "1234567899":
                found = True
        self.assertFalse(found)

    def test_with_zip_code_character(self):
        """TEST WRONG ZIP_CODE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "2800A")
        self.assertEqual("Invalid Zip Code", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__zip_code"] == "2800A":
                found = True
        self.assertFalse(found)

    def test_with_zip_code_length_short(self):
        """TEST WRONG ZIP_CODE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("8421691423220", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "2800")
        self.assertEqual("Invalid Zip Code", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__zip_code"] == "2800":
                found = True
        self.assertFalse(found)

    def test_with_zip_code_length_more(self):
        """TEST WRONG ZIP_CODE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("3662168005326", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "280055")
        self.assertEqual("Invalid Zip Code", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__zip_code"] == "280055":
                found = True
        self.assertFalse(found)

    def test_with_zip_code_not_spain(self):
        """TEST WRONG ZIP_CODE"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.register_order("3662168005326", "PREMIUM", "C/LISBOA,4, MADRID, SPAIN", "123456789",
                                            "53005")
        self.assertEqual("Invalid Zip Code", cm.exception.message)
        json_files_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = json_files_path + "store_request.json"
        with (open(file_store, "r", encoding="UTF-8", newline="")) as file:
            data_list = json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__zip_code"] == "8421691423225":
                found = True
        self.assertFalse(found)
