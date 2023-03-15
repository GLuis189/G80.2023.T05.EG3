"""Module """
import json
import re
import os
from pathlib import Path
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        pattern_rgx = re.compile("[0-9]{13}$")
        valid_pattern = pattern_rgx.match(ean13_code)
        if valid_pattern:
            digits = [int(i) for i in ean13_code]
            sum_pares = 0
            sum_impares = 0
            for i in range(len(digits) - 1):
                if i % 2 == 0:
                    sum_pares += digits[i]
                else:
                    sum_impares += digits[i]
            final = sum_impares * 3 + sum_pares
            valid_digit = 10 - final % 10

            if valid_digit == digits[-1]:
                return True
        return False

    def register_order(self, product_id, order_type, address, phone, zip_code):
        if order_type != "PREMIUM" and order_type != "REGULAR":
            raise OrderManagementException("Invalid Order Type")
        if len(address) < 20 and len(address) > 100:
            raise OrderManagementException("Invalid Address")
        if len(re.findall(" ", address)) == 0:
            raise OrderManagementException("Invalid Address")
        phone_rgx = re.compile("[0-9]{9}$")
        if not phone_rgx.match(phone):
            raise OrderManagementException("Invalid Phone")
        zip_rgx = re.compile("[0-9]{5}$")
        if not zip_rgx.match(zip_code) or (int(zip_code[0]) > 4 and int(zip_code[1]) > 2):
            raise OrderManagementException("Invalid Zip Code")
        valid = self.validate_ean13(product_id)
        if valid:
            my_order = OrderRequest(product_id=product_id, delivery_address=address, order_type=order_type,
                                  phone_number=phone, zip_code=zip_code)
            try:
                with open("file_store.json", encoding = "utf8") as file:
                    data_list = json.load(file)
            except FileNotFoundError as ex:
                raise OrderManagementException("Wrong file or file path") from ex
            except json.JSONDecodeError as ex:
                raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

            try:
                with open("file_store.json", "w", encoding= "utf-8", newline= "") as file:
                    data_list = json.load(file)
                    json.dump(data_list, file, indent=2)
            except FileNotFoundError as ex:
                raise OrderManagementException("Wrong file or file path") from ex
            return my_order.order_id
        raise OrderManagementException("Invalid EAN13 code string")

    def create_json(self, file):
        pass