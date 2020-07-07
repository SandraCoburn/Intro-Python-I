"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

def calendar_input(file="14_cal.py", *args):
  today_date = datetime.now()
  year = today_date.year
  month = today_date.month
  #If the user doesn't specify any input, your program should print the calendar for the current month.
  if len(args) == 0:
    print(calendar.month(year, month, w=0, l=0))
  #user specifies one argument, assume they passed in a month and render the calendar for that month of the current year.
  if len(args) >1:
    try:
      month = int(args[1])
      if month < 1 or month > 12:
        raise ValueError("invalid month")
    except ValueError as err:
      print("invalid format")
      for arg in err.args:
        print(err.args)
      exit()
  if len(args) > 2:
    try:
      year = int(args[2])
    except ValueError as err:
      print("invalid format")
      for arg in err.args:
        print(err.args)
      exit()
  
  # elif len(args) > 1:
  #   year = args[1]
  #   month = args[2]
  #   if year or month:
  #     print(calendar.month(year, month, w=0, l=0))
  # elif len(args) > 2:
  #   year = args[2]
  #   print(calendar.month(year, month, w=0, l=0))
  # else:
  #   print("You need to give the right arguments")
calendar_input(sys.argv)

  


  






  


