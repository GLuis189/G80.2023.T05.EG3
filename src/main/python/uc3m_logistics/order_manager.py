"""Module """
import json
import re
import hashlib
from pathlib import Path
from .order_request import OrderRequest
from .order_management_exception import OrderManagementException
from .order_shipping import OrderShipping
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
        if len(address) < 20 or len(address) > 100:
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
        if not valid:
            raise OrderManagementException("Invalid EAN13 code string")

        my_order = OrderRequest(product_id=product_id, delivery_address=address, order_type=order_type,
                              phone_number=phone, zip_code=zip_code)
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = JSON_STORE_PATH + "store_request.json"
        try:
            with open(file_store,"r", encoding = "utf8") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        data_list.append(my_order.__dict__)

        try:
            with open(file_store, "w", encoding= "utf-8", newline= "") as file:
                #data_list = json.load(file)
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

        return my_order.order_id

    def send_product(self, file_send):
        JSON_STORE_PATH = str(Path.home()) + "\PycharmProjects\G80.2023.T05.EG3\src\JSON\store/"
        file_store = JSON_STORE_PATH + "store_request.json"
        # Abrir el fichero parámetro
        try:
            with open(file_send,"r", encoding = "utf8") as file:
                data_list_send = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Not exist")
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex
        # Comprobar el estado de los parámetros del archivo parámetro
        email_rgx = re.compile("[A-Za-z0-9]+@[a-z0-9.]+.[a-z]{2,3}")
        hash_rgx = re.compile("[a-f0-9]{32}")
        try:
            with open(file_store,"r", encoding = "utf-8") as file:
                data_list_store = json.load(file)
        except FileNotFoundError as ex:
            raise OrderManagementException("Not exist")
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        if not hash_rgx.match(data_list_send["OrderID"]):
            raise OrderManagementException("Invalid hash")
        if not email_rgx.match(data_list_send["ContactEmail"]):
            raise OrderManagementException("Invalid email")
        # Comprobar que el OrderId esté en le almacén
        found = False
        for i in data_list_store:
            if i["_OrderRequest__order_id"] == data_list_send["OrderID"]:
                found = True
                my_order_shipping = OrderShipping(product_id=i["_OrderRequest__product_id"],
                                                  order_id=data_list_send["OrderID"],
                                                  delivery_email=data_list_send["ContactEmail"],
                                                  order_type=i["_OrderRequest__order_type"])
        if not found:
            raise OrderManagementException("OrderId not in store")

        # Crear el fichero alamcen de envios
        file_store_shipping = JSON_STORE_PATH + "store_shipping.json"
        try:
            with open(file_store_shipping,"r", encoding = "utf8") as file:
                data_list = json.load(file)
        except FileNotFoundError as ex:
            data_list = []
        except json.JSONDecodeError as ex:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from ex

        data_list.append(my_order_shipping.__dict__)

        try:
            with open(file_store_shipping, "w", encoding= "utf-8", newline= "") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise OrderManagementException("Wrong file or file path") from ex

        return my_order_shipping.tracking_code()




