# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Module 3 
# Problem 1- input a list of items to be added, then print out the total 
# plus a 7% tax and 15% tip. The tip is of the taxed amount. 
# The main issues that I had with making this program is finding 
# how to do input loops, function returns, and 2 point floats in Python
# References: https://bobbyhadz.com/blog/use-variable-from-another-function-in-python
#             https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points


# input items

def add_stream_of_numbers(sum):
    while True: #This is the way I can make the while loop defer to the ValueError
        try:
            num = float(input("Enter a number (or press Enter to stop): "))
            sum += num
        except ValueError:
            break  # Stop when non-numeric input is provided

    print(f"The sum of the entered numbers is: ")
    print("%.2f " % round(sum, 2))
    
    return sum

# This is to generate the tax, tip, and grand total. Again. tip is calculate cumilatively from
# base plus taxes 
def get_other_values(sum):
    sum = 0 
    sum = add_stream_of_numbers(sum)
    taxes = float( sum * 0.07)
    tip = (sum + taxes) * 0.15
    grand_total = taxes + sum + tip
    print("\n")
    print("The total taxes are: ")
    print("%.2f " % round(taxes, 2))
    print("The total tip is: ")
    print("%.2f " % round(tip, 2))
    print("\n")
    print(f"The grand total is: ")
    print("%.2f " % round(grand_total, 2))
    

get_other_values(sum)
