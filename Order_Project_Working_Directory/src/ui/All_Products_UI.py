from db_logic_pkg.All_Products_DB import All_Products_DB
from db_logic_pkg.Product_DB import Product_DB

class All_Products_UI:
    def __init__(self):
        self.all_products_db= All_Products_DB()

    #appends a new product to the products.txt file
    def input_a_product(self):
        name = input("Enter name of a product: ")
        InputValid = False
        while InputValid == False:
            try:
                unit_price=float(input("Enter the unit price: "))
                InputValid = True
            except Exception as x:
                print("Wrong input type shit")

        stock_count = int(input("Enter the stock count: "))
        p = Product_DB(name,unit_price,stock_count)
        self.all_products_db.save_new_product(p)
            
    '''
    def update_a_product(self)->bool:74
        is_updated=False
        if len(self.all_products_db.all_products)>0:
            print("The following products exist: ")
            self.display_products()
            name = input("Enter the name of the product to update: ")
            for p in self.all_products_db.all_products:
                if name == p.name:
                    print("The current details are: ")
                    print (str(p))                    
                    is_change=input("Do you want to change the unit_price(Y/N)? ")
                    is_change=is_change.lower()
                    if is_change =='y':
                        p.unit_price = float(input("Enter new unitprice: "))
                    is_change=input("Do you want to change the stock count(Y/N)? ")
                    is_change=is_change.lower()
                    if is_change =='y':
                        p.stock_quantity = int(input("Enter new stock count: "))
                    p.update_this_product_in_file()
                    is_updated=True
                    break              

        else:
            print("No existing product")
        return is_updated
'''

    def update_a_product(self) -> bool:
        is_updated = False
        if len(self.all_products_db.all_products) > 0:
            print("The following products exist: ")
            self.display_products()
            name = input("Enter the name of the product to update: ")
        for p in self.all_products_db.all_products:
            if name == p.name:
                print("The current details are: ")
                print(str(p))
                try:
                    change_price = input("Do you want to change the unit price (Y/N)? ").strip().lower()
                    if change_price not in ['y', 'n']:
                        raise ValueError("Please type 'Y' for yes or 'N' for no.")
                    if change_price == 'y':
                        try:
                            p.unit_price = float(input("Enter new unit price: "))
                        except ValueError:
                            print("Please use only numbers for the unit price.")
                            continue

                    change_stock = input("Do you want to change the stock count (Y/N)? ").strip().lower()
                    if change_stock not in ['y', 'n']:
                        raise ValueError("Please type 'Y' for yes or 'N' for no.")
                    if change_stock == 'y':
                        try:
                            p.stock_quantity = int(input("Enter new stock count: "))
                        except ValueError:
                            print("Please use only numbers for the stock count.")
                            continue

                    p.update_this_product_in_file()
                    is_updated = True
                    break
                except ValueError as e:
                    print(e)
                    continue
        else:
            print("No existing product")
        return is_updated