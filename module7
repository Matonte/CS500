# Module 7
class Classes:
    
    room_numbers = {
      'CSC101': '3004', 
      'CSC102': '4501', 
      'CSC103': '6755',
      'NET110': '1244', 
      'COM241': '1411'
    }
    
    instructors = {
      'CSC101': 'Haynes', 
      'CSC102': 'Alvarado', 
      'CSC103': 'Rich',
      'NET110': 'Burke', 
      'COM241': 'Lee'
    }
    
    meeting_times = { 
      'CSC101': '8:00AM', 
      'CSC102': '9:00AM', 
      'CSC103': '10:00AM',
      'NET110': '11:00AM', 
      'COM241': '1:00PM'
    }
    
    
def main():
    
    while(True):
        print("Give a Course else hit x to exit")
        course = input()
        if course == 'x':
            break
        if Classes.room_numbers.get(course) is not None and Classes.instructors.get(course) is not None and Classes.meeting_times.get(course) is not None:
            print("For "+course+" ROOM: "+str(Classes.room_numbers.get(course)))
            print("For "+course+" INSTRUCTOR: "+str(Classes.instructors.get(course)))
            print("For "+course+" TIME: "+str(Classes.meeting_times.get(course)))
        else: 
            print( course+ " is not an offered course!")

        
  
                       
if __name__ == "__main__": main()        
