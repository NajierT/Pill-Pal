# the feature of checking the user's pills for the week 
def pillSchedule(pL):
  
# array of days of the week (which is used to loop)
  daysOfWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  
# loops through each day of the week
  x = 0
  while x < len(daysOfWeek):
    print(daysOfWeek[x], "\n--------------------------------------------------")

# loops through every pill in the main pill list and checks if the day of the week (x) is in the that pill's list of days
# if in the list, pill name and times of day are printed in that day's list
    y = 0
    while y < len(pL):
      temp = pL[y]
      if daysOfWeek[x] in temp[1]:
        print("Pill Name:", temp[0], "\nTimes:", temp[2], "\n")
      else:
        print(temp[0],"not needed")
      y += 1
    print("\n")
    x += 1  