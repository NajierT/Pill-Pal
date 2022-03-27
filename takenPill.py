# allows user to note that they have taken a pill, and subtracts from the pill Total
def takenPill(l):
  
# indexes into pillList and prints name of each pill
  print("Here is a list of your pills: \n")
  x = 0
  while x < len(l):
    print(l[x][0])
    x += 1
    
# matches the user inputted name with a name in pillList
  name = input("What is the name of the pill you took? ")
  y = 0
  while name != l[y][0]:
    y += 1
  temp = l[y][0]

# subtracts a pill from the total amount of the matching pill name
  if name in temp:
    pillsLeft = l[y][3] - 1
    l[y][3] = pillsLeft
  print('You have ' + str(pillsLeft) + ' pills left.')