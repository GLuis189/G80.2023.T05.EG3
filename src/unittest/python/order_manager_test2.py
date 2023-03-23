from unittest import TestCase
from freezegun import freeze_time
from pathlib import Path
from uc3m_logistics import OrderManager

class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_send_product(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = JSON_STORE_PATH + "test1_correct.json"
        my_order=OrderManager()
        my_value = my_order.send_product(file)
        self.assertEqual("19c6f9850bee5e10f75770fd58afb9f79b4951794fec0055ea59c6eb15ac4620",my_value)
