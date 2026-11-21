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
        product = self.search_product(product_id)
        if product is not None:
            product.display_info()
            new_stock = quantity + product.stock
            product.update_stock(new_stock)
        else:
            print("Produk sudah habis")


    def stock_out(self,product_id,quantity):
        product = self.search_product(product_id)
        if product is not None:
            if quantity <= product.stock:
                product.display_info()
                new_stock = product.stock - quantity
                product.update_stock(new_stock)
            else:
                print("Stok tidak mencukupi")
        else:
            print("Produk sudah tidak ada")

    def generate_report(self):
        total_products = len(self.products)
        total_stock = 0
        out_of_stock = 0
        for product in self.products:
            total_stock = total_stock + product.stock

            if product.stock == 0:
                out_of_stock = out_of_stock + 1
        return total_products, total_stock, out_of_stock






keyboard = Product("P-001","Keyboard Razer",1250000,10)
#mouse = Product("P-002","Mouse Razer",675000,8)
inventori = Inventory()
#inventori.add_product(mouse)
inventori.add_product(keyboard)
#keyboard.update_stock(5)
inventori.view_products()
#result = inventori.search_product("P-099")
inventori.stock_in("P-001",5)
inventori.stock_out("P-001",4)
inventori.stock_in("P-001",5)
inventori.stock_out("P-001",20)


total_products, total_stock, out_of_stock = inventori.generate_report()

print("Total Products:", total_products)
print("Total Stock:", total_stock)
print("Out of Stock:", out_of_stock)
inventori.view_products()