import os
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_register_order_okey(self):
        JSON_FILES_PATH = str(Path.home()) + ""
        file_store = JSON_FILES_PATH + "store_order_request.json"
        if os.path.isfile(file_store):
            os.remove(file_store)

        my_order = OrderManager()
        my_value = my_order.register_order(product_id="3662168005326", address="calle colmenarejo",
                                            zip_code="28345", phone="123456789", order_type="premium")
        self.assertEqual("a5d8a05c1d4c9dfd9eb8bf48d23cd804", my_value)
        with (open(file_store,"r", encoding= "UTF-8", newline="")) as file:
            data_list= json.load(file)
        found = False
        for i in data_list:
            if i["_OrderRequest__order_id"] == "a5d8a05c1d4c9dfd9eb8bf48d23cd804":
                found = True
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

    def test_with_address_short(self):
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322", "PREMIUM", "C/LISBOA,4, MADRID ", "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)

    def test_with_address_long(self):
        lista = ["a"]*101
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            value = my_order.register_order("842169142322", str(lista), "PREMIUM", "123456789",
                                            "28005")
        self.assertEqual("Invalid Address", cm.exception.message)

