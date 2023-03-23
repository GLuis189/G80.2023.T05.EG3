from unittest import TestCase
from freezegun import freeze_time
from pathlib import Path
from uc3m_logistics import OrderManager

class TestOrderManager(TestCase):

    @freeze_time("2023-02-19")
    def test_send_product(self):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\send/"
        file = JSON_STORE_PATH + "track.json"
        my_order=OrderManager()
        my_value = my_order.send_product(file)
        return my_value
