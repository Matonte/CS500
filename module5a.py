# Michael Matonte
# June 10 2024
# Module 5 problem 1
#Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
# References 
# https://www.w3schools.com/python/ref_func_range.asp

# created the global variable
months = range(12) 
average = 0.0
total_time = 0
total_rain = 0.0
# get inputted global variables
try:
    print("How many years do you want to add?")
except ValueError:
    print("Bad input.")
else:
    try:
        years = range(int(input()))
        average = 0.0 
            
            # do the double loop and tally things up
        for n in years:
            for m in months:
                print("How much did it rain on " + str(m+1) + "/" + str(n+1) + " ?")
                total_rain += (float(input()))
                total_time += 1 
    except ValueError: 
        print ("That's not a number!")

# do the talley 
try:
    average = total_rain/total_time
except ZeroDivisionError:
    print("no rain recorded.")
print("total recorded time " + str(total_time) + " months")
print("total recorded rain " + str(round(total_rain, 3))+ " inches")
print("average rainfall " + str(round(average,3)) + " inches")
