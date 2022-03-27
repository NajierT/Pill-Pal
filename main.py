# import statements for each file/function
from addPill import addPill
from takenPill import takenPill
from pillSchedule import pillSchedule
from pillStatus import pillStatus

# program starting point

# what did the user type in
action = ''
# initialize main list of all pills
pillList = []

# making it pretty :)
print("Welcome to")
print(" ____  _____  _     _        ____    ____   _")
print("|    |   |    |     |       |    |  |    |  |")
print("|____|   |    |     |       |____|  |____|  |")
print("|        |    |     |       |       |    |  |")
print("|      _____  _____ _____   |       |    |  _____")

# loops and asks user what action they would like to perform
# corresponding function is called, otherwise the program ends
while True:
  action = input("\nWhat would you like to do? \nType 'add' to add a pill: \nType 'taken' to say what pill you took: \nType 'schedule' to see your weekly schedule: \nType 'pills' to check the status of your pills: \nType 'quit' to stop: \n--------------------------------------------------\n")
  if action.lower() == 'add':
    pillList.append(addPill())
  elif action.lower() == 'taken':
    takenPill(pillList)
  elif action.lower() == 'schedule':
   pillSchedule(pillList)
  elif action.lower() == 'pills':
    pillStatus(pillList)
  elif action.lower() == 'quit':
    break