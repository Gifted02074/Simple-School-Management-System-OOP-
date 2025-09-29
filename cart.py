class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def __str__(self):
        return (f"{self.name} price:{self.price}")
class Cart:
    def __init__(self):
        self.products={}
       
        
    def add_product(self,product,quantity):
        if quantity<=0:
            return "negative or zero not accepted "
        if product.name in self.products:
            self.products[product.name]["quantity"]+=quantity
            return "successfully added"
        self.products[product.name]={"product":product,"quantity":quantity}
        
        return "successfully added product"
        
              
    def remove_One_product(self,product):
        if product.name in self.products:
            self.products[product.name]["quantity"]-=1
            if self.products[product.name]["quantity"]==0:
                self.products.pop(product.name)
                return " product removed"
            return "successfully removed one product"
        else:
            return "does not exist"
        

    def remove_per_quantity(self,product,quantity):
        
        if product.name in self.products:
            if self.products[product.name]["quantity"]<quantity:
                return "quantity in cart is less"
            self.products[product.name]["quantity"]-=quantity
            if self.products[product.name]["quantity"]==0:
                self.products.pop(product.name)
                return "product removed"
            return "successfully removed per quantity"
        else:
            return "does not exist"
    def remove_product(self,product):
        if product.name in self.products:
            self.products.pop(product.name)
            return "success"
        else:
            return "does not exist"

    def calculate_total(self):
        total=0
        for a in self.products.values():
            total += a["product"].price*a["quantity"]
        return (total)
    def show_items(self):
        for i in self.products.values():
            print(f"item name:{i["product"].name} quantity:{i["quantity"]} ")
        print(f"total:{self.calculate_total()}")
            
class Customer:
    def __init__(self,name,cart):
        self.cart=cart
        self.name=name
    def show_items(self,cart):
        cart.show_items()

iphone11=Product("iphone 11",200)
dell=Product("laptop",200)
cart1=Cart()
Osei=Customer("Yaw",cart1)
cart2=Cart()
Rabby=Customer("Kofi",cart2)
Jandra=Customer('girl',cart1)
print(Rabby.cart.add_product(dell,2))
# print(Rabby.cart.calculate_total())
print(Jandra.cart.add_product(dell,2))

# print(Jandra.cart.remove_One_product(dell))
print(Jandra.cart.add_product(iphone11,2))
# print(Jandra.cart.calculate_total())
Jandra.cart.show_items()
 
