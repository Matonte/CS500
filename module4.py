# Module 4 
# The only major issue was getting the class and constructor to work 
# Other than that, this was mostly review 
# References: 
# https://www.w3schools.com/python/python_classes.asp
# Create a class called ItemToPurchase 
#item_name (string)
#item_price (float)
#item_quantity (int)
#Default constructor
#Initializes item's name = "none", item's price = 0, item's quantity = 0
#Method
#print_item_cost()
# Class
class ItemToPurchase:
    # Constructor
    def __init__(self, name, price,item_quantity):
        self.name = name
        self.price = price
        self.item_quantity = item_quantity
        
    # Method 
    #Example of print_item_cost() output:
    #Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        cost = round(self.item_quantity * self.price, 2)
        print(self.name +
        " "+ str(self.item_quantity) + " @ $"+ str(round(self.price,2)) +". Item cost is $" +str(cost))
        
# Prompt to create objects and set the values of their attributes 
print("Start giving items") 

print("What's the first item's name?")
name_1 = input()
print("What's the first item's cost?")
price_1 = float(input())
print("How many?")
item_quantity_1 = int(input())
item_1 = ItemToPurchase(name_1,price_1,item_quantity_1)

print("What's the second item's name?")
name_2 = input()
print("What's the second item's cost?")
price_2 = float(input())
print("How many?")
item_quantity_2 = int(input())
item_2 = ItemToPurchase(name_2,price_2,item_quantity_2)

print("\n")
#calculate total
total = (item_1.price * item_1.item_quantity) + (item_2.price * item_2.item_quantity)
#Print one item
item_1.print_item_cost()
item_2.print_item_cost()

# Print the total on next line
print("\nThe total is $%.2f" % round(total, 2))
