# displays pill name, amount left, and how many weeks of pills user has left
def pillStatus(pL):
  
  x = 0
# creates header
  print("\n ***** PILL STATUS *****")

# indexes into pillList and stores each pill in temp 
  while x < len(pL):
    temp = pL[x]

# prints info about specified pill
    print("\n--------------------------------------------------\nPill Name:", temp[0])
    print(temp[0], "has", temp[3], "pills left.")
    x = x+1
    weeksLeft = int(temp[3]/temp[4])
    print(temp[0], "has", weeksLeft, "weeks left." )

# displays a warning message if there are less than 2 weeks worth of pills remaining
    if weeksLeft <= 2:
      print('\n\nWARNING: !!!!!!!!!!')
      print("\nYou have "+  str(weeksLeft) + " weeks left of your pills, please contack your provider.\n")
      print("WARNING: !!!!!!!!!!\n")
