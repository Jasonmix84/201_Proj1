"""
File: p1.py
Author: Jason Rojas
Date: 10/31/22
Lab Section: 42
Email:  jasonr2@umbc.edu
Description:  This program shows the layout of code in a Python file, and greets
the user with the name of the programmer
"""

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''
debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data

''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''

def list_students_not_in_class(class_roster, if_present):
   """
   Compare the swipe log with the given course roster. Place those students that
   did not show up for class into a list.
   :param Class_roster: list of students from fill_roster  
   :param if_present: Entries of students including names, time of entrance, and date
   :return: no_show a list of of names not in if_present
   """
   #Gets all numbers in if_present
   new_if_present = []
   for i in if_present:
      i = i[-1:-23:-1]
      i = i[::-1]
      new_if_present.append(i)
      
   #removes them by leaving only names   
   j = 0
   index = 0
   final_if_present = []
   for i in if_present:
      final_if_present.append( i.rstrip(new_if_present[index]) )
      j += 1
      index += 1

   #if the name is not in the roster add it to no_show list
   no_show = []
   for i in class_roster:
      if i not in final_if_present:
         no_show.append(i)

   return no_show

def list_all_times_checking_in_and_out(student, if_present):
   """
   Looking at the swiping log, this function will list all in and outs for a
   particular Student. Please note, as coded in the p1.py file given, this
   function was called three times with different student values. 
   :param student: a given input that is used to find data and output that data
   :param if_present: Entries of students including names, time of entrance, and date
   :return: in_and_out a list of data of student
   """
   #if the student starts with the index it is checking then add it to a list and output the info
   in_and_out = []
   for i in if_present:
      if i.startswith(student):
         in_and_out.append(i)
         
   return in_and_out
         
def list_all_times_checked_in(if_present):
   """
   This function returns a list of when all student(s) FIRST swipe in. 
   :param if_present: Entries of students including names, time of entrance, and date 
   :return: list of data from entries of students that were present
   """
   #Gets all numbers in if_present
   new_if_present = []
   for i in if_present:
      i = i[-1:-23:-1]
      i = i[::-1]
      new_if_present.append(i)

   #removes them by leaving only names
   j = 0
   index = 0
   final_if_present = []
   for i in if_present:
      final_if_present.append( i.rstrip(new_if_present[index]) )
      j += 1
      index += 1
      
   #go through list and if person name not in the list add them should add everyone only the first time
   entries_of_person = []
   log_ins = []
   for i in final_if_present:
      if i not in entries_of_person:
         entries_of_person.append(i)

   #find the values using the number of index in our list above and then add the outpot to list of log_ins
   indice = 0
   for i in entries_of_person:
       log_ins.append(if_present[indice]) 
       indice += 1
       
   return log_ins
          
def list_students_late_to_class(time, if_present):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param A given string that represents a time which represents a point where anything after is considered late
    :param if_present: Entries of students including names, time of entrance, and date
    :return: late_list: a list of students that pass the param time
    """
   
    only_times = []
    for i in list_all_times_checked_in(attendData):
    #gets a list of only times
        i = i[-12:-21:-1]
        i = i[::-1]
        only_times.append(i)

    #splits times into lists of hours and mins and secs
    hours_list = []
    mins_list = []
    secs_list = []
    for times in only_times:
        hours = times[0:2]
        mins = times[3:5]
        secs = times[6:8]

        hours = int(hours)
        mins = int(mins)
        secs = int(secs)

        hours_list.append(hours)
        mins_list.append(mins)
        secs_list.append(secs)   

   #convert all times to secs
    hrs_in_sec = []
    mins_in_sec = []
    for hours in hours_list:
        hours = hours * 3600
        hrs_in_sec.append(hours)
    for mins in mins_list:
        mins = mins * 60
        mins_in_sec.append(mins)

    #Puts the sum of the secs in a list
    all_times_in_secs = []
    index = 0
    for i in range(len(hrs_in_sec)):
        hrs_plus_mins = hrs_in_sec[i] + mins_in_sec[index]
        hrs_mins_secs = hrs_plus_mins + secs_list[index]
        all_times_in_secs.append(hrs_mins_secs)
        index += 1
    #write code here for changing the given time to sec
    time_list = time.split(':')
    hour = int(time_list[0])
    minute = int(time_list[1])
    second = int(time_list[2])
    time_in_sec = (hour*3600) + (minute*60) + (second*1)

    #check if the time in sec of the time is less than the students entry times
    index_list = []
    for time in range(len(all_times_in_secs)):
       if all_times_in_secs[time] > time_in_sec:
          index_list.append(time)
    #get a list of late students
    late_list = []
    for i in index_list:
        late_list.append(if_present[i])
    return late_list
        
   
   
def get_first_student_to_enter(if_present):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param if_present: Entries of students including names, time of entrance, and date
    :return: first_student_to_enter: a list that contains the first student to enter
    """
    #gets all numbers
    new_if_present = []
    for i in if_present:
       i = i[-1:-23:-1]
       i = i[::-1]
       new_if_present.append(i)
      
    #list of only names by removing all numbers
    j = 0
    index = 0
    final_if_present = []
    for i in if_present:
       final_if_present.append( i.rstrip(new_if_present[index]) )
       j += 1
       index += 1
    
    #gets a list of only times
    only_times = []
    for i in if_present:
       i = i[-12:-21:-1]
       i = i[::-1]
       only_times.append(i)
    
    #splits times into lists of hours and mins and secs
    hours_list = []
    mins_list = []
    secs_list = []
    for times in only_times:
       hours = times[0:2]
       mins = times[3:5]
       secs = times[6:8]

       hours = int(hours)
       mins = int(mins)
       secs = int(secs)

       hours_list.append(hours)
       mins_list.append(mins)
       secs_list.append(secs)
       
    #convert all times to secs
    hrs_in_sec = []
    mins_in_sec = []
    for hours in hours_list:
       hours = hours * 3600
       hrs_in_sec.append(hours)
    for mins in mins_list:
       mins = mins * 60
       mins_in_sec.append(mins)
       
    #Puts the sum of the secs in a list
    all_times_in_secs = []
    index = 0
    for i in range(len(hrs_in_sec)):
       hrs_plus_mins = hrs_in_sec[i] + mins_in_sec[index]
       hrs_mins_secs = hrs_plus_mins + secs_list[index]
       all_times_in_secs.append(hrs_mins_secs)
       index += 1

    #Check for smallest value and then output it
    lowest_time = all_times_in_secs[0]
    for times in range(len(all_times_in_secs)-1):
       if all_times_in_secs[times - 1] < lowest_time:
          lowest_time = all_times_in_secs[times - 1]

    #remake lowest_time into the hh:mm:ss format to check which student has that time to output
    first_student_orig_time = []
    working_lowest_time = lowest_time

    first_student_hrs = working_lowest_time // 3600
    working_lowest_time = working_lowest_time - (first_student_hrs * 3600)
    first_student_orig_time.append("0"+str(first_student_hrs))
    
    first_student_mins = working_lowest_time // 60
    working_lowest_time = working_lowest_time - (first_student_mins * 60)
    first_student_orig_time.append(str(first_student_mins))
    
    first_student_orig_time.append(str(working_lowest_time)+',')

    check_time = ':'.join(first_student_orig_time)

    #check if the lowest time is in the if_present list and keep adding to a indice counter until it is in it then use that indice number to return that indice from the list of only names
    indice = 0
    first_student_to_enter = []
    for i in if_present:
       while check_time not in if_present[indice]:
          indice += 1
    first_student_to_enter.append(final_if_present[indice])
    
    return first_student_to_enter

def printList(any_func):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param any_func: a called upon function 
    :return: none
    """
    for i in any_func:
        print(i)                       

''' ***** LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE ***************
********* LEAVE THE LINES BELOW ALONE *************** '''

if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class    
    
    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here
    
    #load data
    attendData = fill_attendance_data()
    
    #use different tests 
    # make sure roster was filled 
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)
    
    #list all those missing
    print("****** Students missing in class *************")    
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))  
    #display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))  
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
    #display first student to enter class
    print("******* Get 1st student to enter class ****************")    
    print(get_first_student_to_enter(attendData))
    
''' ***** LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE ***************
********* LEAVE THE LINES ABOVE ALONE *************** '''
