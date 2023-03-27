"""MODULES"""
import os
from pathlib import Path
from unittest import TestCase
from freezegun import freeze_time
from uc3m_logistics import OrderManager
from uc3m_logistics import OrderManagementException

class TestOrderManager(TestCase):
    """CLASS TEST3 ORDER DELIVERY"""

    @freeze_time("2023-02-19")
    def crear_my_order_premium(self):
        """CREATE ORDER_PREMIUM DELIVERY"""
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="PREMIUM")
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test1_correct.json"
        return my_order.send_product(file)

    @freeze_time("2023-02-19")
    def crear_my_order_regular(self):
        """CREATE ORDER_REGULAR DELIVERY"""
        my_order = OrderManager()
        my_order.register_order(product_id="3662168005326", address="C/LISBOA,4, MADRID, SPAIN",
                                zip_code="28345", phone="123456789", order_type="REGULAR")
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = json_store_path + "test1_correct_r.json"
        return my_order.send_product(file)



    @freeze_time("2023-02-26")
    def test_deliver_product_regular(self):
        """TEST OKEY ORDER_REGULAR DELIVERY"""
        my_order = OrderManager()
        delivery = my_order.deliver_product(self.crear_my_order_regular())
        self.assertTrue(delivery)

    @freeze_time("2023-02-20")
    def test_deliver_product_premium(self):
        """TEST OKEY ORDER_PREMIUM DELIVERY"""
        my_order = OrderManager()
        delivery = my_order.deliver_product(self.crear_my_order_premium())
        self.assertTrue(delivery)

    def test_deliver_path1(self):
        """TEST PATH1"""
        my_order = OrderManager()
        hash_delivery = "x"
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product(hash_delivery)
        self.assertEqual("Invalid tracking number" , cm.exception.message)

    def test_deliver_path2(self):
        """TEST PATH2"""
        my_order = OrderManager()
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store_shipping = json_store_path + "store_shipping.json"
        if os.path.isfile(file_store_shipping):
            os.remove(file_store_shipping)
        hash_delivery = "6d32ac3991586ab58f8ff2ddf4a2de61f35a46f6bdc20121c5f57a91f0f6ccd4"
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product(hash_delivery)
        self.assertEqual( "File doesn't exist", cm.exception.message)

    @freeze_time("2023-02-20")
    def test_deliver_path3(self):
        """TEST PATH3"""
        my_order = OrderManager()
        my_order.deliver_product(self.crear_my_order_premium())
        hash_delivery = "6d32ac3991586ab58f8ff2ddf4a2de61f35a4688bdc20121c5f57a91f0f6ccd4"
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product(hash_delivery)
        self.assertEqual("Not found tracking number", cm.exception.message)


    def test_deliver_path4_premium(self):
        """TEST PATH4_PREMIUM"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product(self.crear_my_order_premium())
        self.assertEqual("Incorrect delivery date", cm.exception.message)

    def test_deliver_path4_regular(self):
        """TEST PATH4_REGULAR"""
        my_order = OrderManager()
        with self.assertRaises(OrderManagementException) as cm:
            my_order.deliver_product(self.crear_my_order_regular())
        self.assertEqual("Incorrect delivery date", cm.exception.message)

    @freeze_time("2023-02-20")
    def test_deliver_path5_premium(self):
        """TEST PATH5_PREMIUM"""
        my_order = OrderManager()
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store_delivery = json_store_path + "store_delivery.json"
        if os.path.isfile(file_store_delivery):
            os.remove(file_store_delivery)
        delivery = my_order.deliver_product(self.crear_my_order_premium())
        self.assertTrue(delivery)

    @freeze_time("2023-02-26")
    def test_deliver_path5_regular(self):
        """TEST PATH5_REGULAR"""
        my_order = OrderManager()
        json_store_path = str(Path.home()) + r"\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store_delivery = json_store_path + "store_delivery.json"
        if os.path.isfile(file_store_delivery):
            os.remove(file_store_delivery)
        delivery = my_order.deliver_product(self.crear_my_order_regular())
        self.assertTrue(delivery)

    @freeze_time("2023-02-20")
    def test_deliver_path6_premium(self):
        """TEST PATH6_PREMIUM"""
        my_order = OrderManager()
        delivery = my_order.deliver_product(self.crear_my_order_premium())
        self.assertTrue(delivery)

    @freeze_time("2023-02-26")
    def test_deliver_path6_regular(self):
        """TEST PATH5_REGULAR"""
        my_order = OrderManager()
        delivery = my_order.deliver_product(self.crear_my_order_regular())
        self.assertTrue(delivery)
