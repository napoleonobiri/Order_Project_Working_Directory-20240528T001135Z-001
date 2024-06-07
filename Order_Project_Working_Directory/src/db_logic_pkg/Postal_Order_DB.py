import os
import sys
sys.path.append("../..")
from datetime import datetime
from Order_DB import Order_DB

class Postal_Order_DB(Order_DB):
    postal_file_name = 'postal_orders.txt'

    def save(self):
        super().save()  # Call the save method from Order_DB to handle the order part

        # Handle the postal order specifics
        try:
            postal_path = Order_DB.file_path + Postal_Order_DB.postal_file_name
            # Create file if not created already
            if not os.path.isfile(postal_path):
                with open(postal_path, 'x') as f:
                    pass

            with open(postal_path, "a") as f:

                tracking_info = f"{self.order['order_id']},{datetime.now().strftime('%d%m%Y')},Initiated->Packed->Shipped->Delivered\n"
                f.write(tracking_info)      
        except Exception as e:
            print("Error in saving postal order: " + str(e))

    @staticmethod
    def read_order():
        # Implementation for reading a postal order
        pass

    def update_this_order_in_file(self):
        # Implementation for updating a postal order in file
        pass

    def __str__(self):
        # Extend the string representation to include postal order details if needed
        base_str = super().__str__()
        return base_str + ", Status: Delivered"
