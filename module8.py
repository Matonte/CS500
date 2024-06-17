# Module 8 
#
class ShoppingCart:
    #Constructor
        
    def __init__(self, customer_name= "None", current_date= "January 1, 2020",cart_items =[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    

    def add_item(self,item):
        self.cart_items.append(item)
    
    def remove_item(self,item_name):
        print(item_name)
        item = ItemToPurchase(item_name)
        for i in self.cart_items:
            print(i.name)
            if i.name == item.name:
               self.cart_items.remove(i)
               print("Item removed.")
               break
            else: 
               print("Item not found in cart. Nothing removed.")
    
    def modify_item(self,ItemToPurchase):
        if ItemToPurchase.name == "None":
            print("What's item's name?")
            ItemToPurchase.name = input()
        if ItemToPurchase.item_description == "None":
            print("What's item's description?")
            ItemToPurchase.item_description = input()
            if ItemToPurchase.price == 0.0:
                try:
                    print("What's item's price?")
                    ItemToPurchase.price = float(input())
                except  ValueError:
                    print("Bad input")
            if ItemToPurchase.item_quantity == 0:
                try:
                    print("how many?")
                    ItemToPurchase.item_quantity = int(input())
                except  ValueError:
                    print("Bad input")
        else:
            print(" Item not found in cart. Nothing modified.")
            
    def modify_quantity(self):
        print("What is the item?")
        item = ItemToPurchase()
        item.name = input()
        for i in self.cart_items:
            print (i)
            print( i.name)
            if i.name == item.name:
                item = i
        if item in self.cart_items:
            try:
                print("how many?")
                item.item_quantity = int(input())
            except  ValueError:
                print("Bad input")
        else:
            print(" Item not found in cart. Nothing modified.")
    
    def get_num_of_items_in_cart(self):
        return len(self.cart_items)
    
    
    def cost_of_cart(self):
        total = 0.0
        for item in list(self.cart_items):
            total += (item.price * item.item_quantity)
        return round(total, 2)
    
    def print_total(self):
        total = 0.0
        if self.get_num_of_items_in_cart() > 0:
            print("\n" + self.customer_name+"'s Shopping Cart" +"- "+ self.current_date)
            for item in list(self.cart_items):
                total += (item.price * item.item_quantity)
                item.print_item_cost()
            print("\nThe total is $%.2f" % round(total, 2))
        else: 
            print("SHOPPING CART IS EMPTY")
        
    def print_descriptions(self):
        print("\n" + self.customer_name+"'s Shopping Cart" +"- "+ self.current_date)
        print("\nItem Descriptions")
        for item in list(self.cart_items):
            print(item.name+": "+item.item_description)

    
# Class
class ItemToPurchase:
    # Constructor
    def __init__(self, name= "None", price = 0.0 ,item_quantity= 0,item_description="None"):
        self.name = name
        self.price = price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    # Method 
    #Example of print_item_cost() output:
    #Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        cost = round(self.item_quantity * self.price, 2)
        print(self.name +
        " "+ str(self.item_quantity) + " @ $"+ str(round(self.price,2)) +". Item cost is $" +str(cost))
        
# Prompt to create objects and set the values of their attributes 

def print_menu():
    
    print("                    ~~WECLOME~~")
    print("What is your name?")
    name = input()
    print("What is the date?")
    date = input()
    cart =  ShoppingCart(name,date)
    item_0 = ItemToPurchase("Things",99.99,4," it has to do deal with things.")
    item_1 = ItemToPurchase("Stuff",49.99,6," those things DO involve stuff!")
    cart.add_item(item_0)
    cart.add_item(item_1)
    for i in cart.cart_items :
        print(i.name)
    print("                       MENU     ")
    while(True):
        print("pick an option:")
        print("q- quit")
        print("a- Add an item")
        print("r- remove an item")
        print("c- change item quantity")
        print("i - output items' descriptons")
        print("o - output shopping cart")
        answer = input()
        if answer == 'q':
            break
        elif answer == 'c':
            cart.modify_quantity()
        elif answer == 'a':
            item  = ItemToPurchase()
            cart.modify_item(item)
            cart.add_item(item)
            cart.print_total()
            print("item added")
        elif answer == 'r':
            print(cart.get_num_of_items_in_cart())
            print("What item do you want to remove?")
            item = input()
            cart.remove_item(item)
            print(cart.get_num_of_items_in_cart())
            print
        elif answer == 'i':
            cart.print_descriptions()
        elif answer == 'o':
            cart.print_total()

def main(): 
    print_menu()
                       
if __name__ == "__main__": main()    
