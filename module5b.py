# Michael Matonte
# June 10 2024
# Module 5 problem 2
#The CSU Global Bookstore has a book club that awards points to its students based on the number of books purchased each month. The points are awarded as follows:

#    If a customer purchases 0 books, they earn 0 points.
##    If a customer purchases 2 books, they earn 5 points.
#    If a customer purchases 4 books, they earn 15 points.
#    If a customer purchases 6 books, they earn 30 points.
#    If a customer purchases 8 or more books, they earn 60 points.
 #   Write a program that asks the user to enter the number of books that they have purchased this month and then display the number of points awarded.
# References 
# https://www.w3schools.com/python/ref_func_range.asp
#create global variables 
points = 0
# input
print("how many books did you buy?")
books = int(input())

#conditional logic for problem. Designed in a way that gives the right amount of points 
# in a descending way 
if books > 7:
    points = 60
elif books > 5:
    points = 30
elif books > 3:
    points = 15
elif books > 1:
    points = 5

# print the answer 
print("You have earned " + str(points)+".")
