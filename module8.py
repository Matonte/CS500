# Module 8 
#
#Shopping Cart Class
class ShoppingCart:
    #Constructor w/ default variables
        
    def __init__(self, customer_name= "None", current_date= "January 1, 2020",cart_items =[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
# basic add item function
    def add_item(self,item):
        self.cart_items.append(item)
        
# remove item that uses polling with a dummy object to find item to remove
    def remove_item(self,item_name):
        found = False
        item = ItemToPurchase(item_name)
        for i in self.cart_items:
            if i.name == item.name:
               self.cart_items.remove(i)
               print("Item removed.")
               found = True
               break
        if found is False:
               print("Item not found in cart. Nothing removed.")

# Will create the details of an item if there are currently none 
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

# uses dummy object, as assignment suggested
    def modify_quantity(self):
        print("What is the item?")
        item = ItemToPurchase()
        item.name = input()
        for i in self.cart_items:
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

#  simple wrapper function to return number of items
    def get_num_of_items_in_cart(self):
        return len(self.cart_items)
    
# Cost of cart function
    def cost_of_cart(self):
        total = 0.0
        for item in list(self.cart_items):
            total += (item.price * item.item_quantity)
        return round(total, 2)
 
 # Print function  
    def print_total(self):
        total = 0.0
        if self.get_num_of_items_in_cart() > 0:
            print("\n" + self.customer_name+"'s Shopping Cart" +"- "+ self.current_date)
            for item in list(self.cart_items):
                total += (item.price * item.item_quantity)
                item.print_item_cost()
            print("\nThe total is $%.2f" % round(total, 2))
            print("\n")
        else: 
            print("SHOPPING CART IS EMPTY")
 # Description function        
    def print_descriptions(self):
        print("\n" + self.customer_name+"'s Shopping Cart" +"- "+ self.current_date)
        print("\nItem Descriptions")
        for item in list(self.cart_items):
            print(item.name+": "+item.item_description)

    
# Class for terms 
class ItemToPurchase:
    # Constructor with default variables 
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
        
# Print the menu 
def print_menu():
    
    print("                    ~~WECLOME~~")
    print("What is your name?")
    name = input()
    print("What is the date?")
    date = input()
    cart =  ShoppingCart(name,date)
    
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
            print("QUITTING")
            break
        elif answer == 'c':
            print("MODIFYING ITEM QUANTITY")
            cart.modify_quantity()
    
        elif answer == 'a':
            print("ADD ITEM TO CART")
            item  = ItemToPurchase()
            cart.modify_item(item)
            cart.add_item(item)
            print("item added")
        elif answer == 'r':
            print("REMOVE ITEM FROM CART")
            print("What item do you want to remove?")
            cart.remove_item(input())
            print
        elif answer == 'i':
            print("CART DESCRIPTIONS")
            cart.print_descriptions()
        elif answer == 'o':
            print("CART CONTENTS AND PRICE")
            cart.print_total()
            
# Main method
def main(): 
    print_menu()
                       
if __name__ == "__main__": main()    
