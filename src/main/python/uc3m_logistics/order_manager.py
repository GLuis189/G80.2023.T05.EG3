"""Module """
from .order_request import OrderRequest
class OrderManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    @staticmethod
    def validate_ean13(ean13_code):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        pattern_rgx = re.compile("[0-9]{13}")
        valid_pattern = pattern_rgx.match(ean_13)
        if valid_pattern:
            digits = [int(i) for i in ean_13]
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
                print("El código cumple con el estandar EAN13")
                return True
        print("El código no cumple con el estandar EAN13")
        return False

    def register_order(self,product_id,adress,ordeer_typt,phone,zip_code):
        my_order=OrderRequest(product_id=product_id, delivery_address=address, order_type=order_type
                              phone_number=phone, zip_code=zip_code)
        return my_order.order_id
