# the feature of adding a pill to the existing list of pills 
def addPill():
  
# user inputting info about their medication
  name = input("Enter the name of the pill: \n")
  days = input("Enter the days you need to take the pill (comma seperated list): \n")
  daysList = days.split(", ")
  totalPills = int(input("Enter the total amount of pills in the bottle: \n"))
  timesPerDay = input("Enter the times of day you need to take the pill (comma seperated list; options are 'morning', 'afternoon', and/or 'night'): \n") 
  timesList = timesPerDay.split(", ")
  
# calculating the number of pills a user takes per week  
  numPerWeek = len(daysList) * len(timesList)

  # adding all inputs into an array
  info = [name, daysList, timesList, totalPills, numPerWeek]

  # return array with info (which gets appended to main pill list array in main file)
  return info 