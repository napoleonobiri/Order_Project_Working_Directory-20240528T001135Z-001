import os
import sys
from order_app_logic_pkg.Order import Order
sys.path.append("../..")


#from src.order_app_logic_pkg.Order import Order

# from ui.Order_mgt_UI import create_order
# from ui.Order_mgt_UI import create_order_item

class Order_DB:
    file_path = os.sep + 'assets' + os.sep + 'data_files' + os.sep
    file_name = 'orders.txt'

    header_template = '{:12},{:8},{:5}\n'
    customer_template = '{:10},{:25},{:30}\n'
    item_tempalte = '{:50},{:10.2f},{:5d}\n'
    def __init__(self, order:Order=None):
        #if order:
        self.order = order
        #else:
        #    self.order = {
         #       'order_id': '',
          #      'order_date': '',
           #     'customer_id': '',
           #     'customer_name': '',
            #    'customer_email': '',
           #     'order_items': []
            

    def save(self):
        try:
            # Create file if not created already
            if not os.path.isfile(Order_DB.file_path + Order_DB.file_name):
                f = open(Order_DB.file_path + Order_DB.file_name, 'x')
                f.close()

            # Open the file in append mode
            f = open(Order_DB.file_path + Order_DB.file_name, "a")
            f.write(Order_DB.header_template(self.order_id,self.order_date,len(self.order.items)))
            f.write(Order_DB.customer_template(self.order.customer_id,self.cust_name,self.cust_email))
            f.write(Order_DB.item_template(self.order.item_name,self.item_unit_price,self.cust_item_qty))
            '''2b
        self.order_id=str(Order.order_num)
        self.customer = customer
        self.order_date= datetime.now()
        self.items = []  # Initialize an empty list to store order items


                ))'''

            f.close()
        except Exception as e:
            print("Error: " + str(e))
    def __str__(self):
        return f"Order ID: {self.order['order_id']}, Customer: {self.order['customer_name']}"
    
