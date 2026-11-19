class Product():

    def __init__(self,product_id,product_name,price,stock):
        self.product_id = product_id
        self.product_name  = product_name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(self.product_id)
        print(self.product_name)
        print(self.price)
        print(self.stock)

    def update_stock(self, new_stock):
        self.stock = new_stock



class Inventory():

    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)

    def view_products(self):
        for product in self.products:
            product.display_info()

    def search_product(self,product_id):
        for product in self.products:
            if product_id == product.product_id:
                return product
        return None

    def stock_in(self,product_id,quantity):
        




keyboard = Product("P-001","Keyboard Razer",1250000,10)
mouse = Product("P-002","Mouse Razer",675000,8)
inventori = Inventory()
inventori.add_product(mouse)
inventori.add_product(keyboard)
keyboard.update_stock(5)
inventori.view_products()
result = inventori.search_product("P-099")
if result is not None:
    result.display_info()
else:
    print("Produk Tidak ada")
