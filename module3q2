# Problem 2- Give a time in hours and a number of hours and return the
# the hour it will be after the alloted hours 
# This program was more straight-forward and didn't use any additional concepts
# 


def give_the_time():
    hour = 0
    time = 0
    try: #have a way to handle bad input
        print("What is the hour?")
        hour = int(input())
        print("what is the time?")
        time = int(input())
    except ValueError:
        print("Put in numbers only.")
        return "not a number"
    # logic happens here     
    return (hour+time) % 24
    
    
print("Then the time will be",give_the_time())
