# My_Mario_Game.py
# Description: Mario Location Game
# Author: Himani Boury
# Date: Aug. 2019

  
def readDataFileAndSetVariables( filename ):
    # Make the following variables accessible in this function by making them "global"
    global mazeWidth
    global mazeHeight
    global aNumOfTreasures
    global aNumOfBombs
    global emptyCell
    global treasure
    global bomb
    global mario
    global exitGate
    global boundary
    global boundarySide
    global marioLocationList
    global rList
    global eList
    global bombScoreRatio

    # Open file for reading
    dataFileRead = open(filename, "r")

    # Read file content into a list - to be completed - Part 1
    items = []
    for line in dataFileRead:
        items.append(line.strip())
    

    mazeWidth = int(items[0])
    mazeHeight = int(items[1])
    aNumOfTreasures = int(items[2])
    aNumOfBombs = int(items[3])

    emptyCell = " " + str(items[4]) + " "
    treasure = " " + str(items[5]) + " "
    bomb =  " " + str(items[6]) + " "
    mario = " " + str(items[7]) + " "
    exitGate = " " + str(items[8]) + " "
    boundary = str(items[9])
    boundarySide = str(items[10])

    bombScoreRatio = int(items[-1])
    myList = items[12:60]

    locationList.append(items[11][0])
    locationList.append(items[11][2])

    temp5List.append(int(locationList[0]))
    temp5List.append(int(locationList[1]))

    marioLocationList = [temp5List[0:2]]

    for j in range(0, 45):
      tempList.append(myList[j][0])
      xList.append(tempList[j])

    for y in range(0, 45):
      temp2List.append(myList[y][2])
      yList.append(temp2List[y])

    temp3List = [[] for k in range(len(myList))]
    
    for h in range(0,45):
      temp3List[h].append(int(xList[h]))
      temp3List[h].append(int(yList[h]))

    rList = temp3List[0:15]
    eList = temp3List[15:-1]

  
  # For debugging purposes
    #print("maze widht = ", mazeWidth)
    #print("mazeHeight = ", mazeHeight)
    #print("aNumOfTreasures = ", aNumOfTreasures)
    #print("aNumOfBombs = ", aNumOfBombs)
    #print("emptyCell = '{}'".format(emptyCell))
    #print("treasure = '{}'".format(treasure))
    #print("bomb = '{}'".format(bomb))  
    #print("mario = '{}'".format(mario))    
    #print("exitGate = '{}'".format(exitGate))
    #print("boundary = '{}'".format(boundary))    
    #print("boundarySide = '{}'".format(boundarySide))
    #print("marioLocationList = ", marioLocationList)
    #print("rList = ", rList)
    #print("eList = ", eList)
    #print("bombScoreRatio = ", bombScoreRatio)

    # Close the file
    dataFileRead.close( )
    return

# -------------------------------------------------------------------

def createMaze(aMaze, aWidth, aHeight, aCell):
    ''' Create and return "aMaze" of "aWidth" by "aHeight".
        Each cell of the maze is a string set to "cell".      
    '''
    aMaze = [ [ (aCell) for i in range(aWidth) ] for j in range(aHeight) ]   
    return aMaze

# -------------------------------------------------------------------

# Print Maze - for debugging purposes
def printMaze(aMaze, aHeight):
    ''' Print "aMaze" of "aHeight" - for debug purposes.
    ''' 
    for row in range(aHeight):
        print(aMaze[row])  
    return
		
# -------------------------------------------------------------------

def createBoundary(aWidth, bH):
    ''' Create and return a list that contains 2 lists: the top boundary of the maze
        and the bottom boundary of the maze. Each element of these 2 lists is a string set to "bH".
    '''
    return list([[(bH) for number in range(aWidth)],[(bH) for number in range(aWidth)]])                

# -------------------------------------------------------------------

def displayMaze(aMaze, aWidth, aHeight, hBoundary, bS ):
    ''' Display 'aMaze' with column numbers at the top and row numbers to the left of each row
        along with the top and the bottom boundaries "hBoundary" that surround the maze.

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.
         "bS" is the symbol used for the vertical border.

        No returned value
    '''
    topIndex = 0  # Index of proper boundary in hBoundary
    bottomIndex = 1
    offset = 3
    aString = (offset+1) * " "

    print()  
    # Display a row of numbers from 1 to aWidth
    for column in range(aWidth):
        aString = aString + str(column+1) + " "
        if len(str(column+1)) == 1 :
            aString += " "           
    print(aString)

    # Display the top boundary of maze
    print(offset * " " + "".join(hBoundary[topIndex]))
    
    # Display a column of numbers from 1 to aHeight + left and right boundaries of the maze
    for row in range(aHeight):
        pre = str(row+1) + " " + bS
        if row >= 9: # i.e., displayed row number is >= 10 - adjusting for extra digit
           pre = str(row+1) + bS
        post = bS
        aRow = pre + ''.join(aMaze[row]) + post
        print(aRow)

    # Display the bottom boundary of maze
    print(offset * " " + "".join(hBoundary[bottomIndex]))
    return

# -------------------------------------------------------------------

def placeInMaze(aMaze, aRow, aColumn, aContent):
    ''' Place something represented by "aContent" at the location ["aRow", "aColumn"] into "aMaze"

        Returned value:
         "aMaze" updated.
    '''
    aMaze[aRow][aColumn] = aContent
    return aMaze

# -------------------------------------------------------------------

def placeExitGate(aWidth, aHeight, rowMario, columnMario, hBoundary, exitGate):
    ''' Place the exit gate, represented by "exitGate", at the opposite corner of Mario's location.
		This means:
		Place the exit gate either in the top boundary or the bottom boundary 
		which ever is at the opposite corner of Mario's location, represented by [rowMario, columnMario].

        Other parameters:
         "aWidth" is the width of the maze.
         "aHeight" is the height of the maze.

        Returned value:
         "hBoundary" updated.
         "hBoundary" is a list of 2 lists: the first list is the top boundary and the second list is the bottom boundary.
         "exitGateLocationList" updated.
    '''
    topIndex = 0 # Index of proper boundary in hBoundary
    bottomIndex = 1
    exitGateRight = False
    exitGateBottom = False
    row = 0
    column = 1
    exitGateLocationList.insert(row, 0)   # Assume exit gate at the top left
    exitGateLocationList.insert(column, 0)
        
    # Where is Mario?
    # If Mario is top left then exit gate is bottom right
    if columnMario <= ((aWidth) // 2) : # Mario on the left?
        exitGateLocationList[column] = aWidth - 1  # Yes, then exit gate on the right
        exitGateRight = True
    # No, then assuption holds -> exit gate on the left
    if rowMario <= ((aHeight) // 2) :   # Mario at the top?
        exitGateLocationList[row] = aHeight - 1    # Yes, then exit gate at the bottom
        exitGateBottom = True
        # No, then assuption holds -> exit gate at the top

    # Place exit gate in appropriate top/bottom boundary
    if exitGateBottom :
        del hBoundary[bottomIndex][exitGateLocationList[column]]
        hBoundary[bottomIndex].insert(exitGateLocationList[column], exitGate)
    else:
        del hBoundary[topIndex][exitGateLocationList[column]]
        hBoundary[topIndex].insert(exitGateLocationList[column], exitGate)       

    
    return hBoundary, exitGateLocationList  # Can return a tuple -> elements sepatared by a coma

# -------------------------------------------------------------------

def setMarioScore(numOfBombs, divideBy):
    ''' Set and return Mario's score to be numOfBombs // divideBy
    '''    
    return numOfBombs // divideBy

# -------------------------------------------------------------------


# Main part of the program

# Welcome the user and identify the game
print("""Welcome to my Mario game.\n""")

# Ask user for filename
filename = input("Please, enter a filename: ")

# Initialize the game variables ...
mazeWidth = 0
mazeHeight = 0
aNumOfTreasures = 0
aNumOfBombs = 0
emptyCell = ""
treasure = "" 
bomb = ""
mario = ""  
exitGate = ""  
boundary = ""  
boundarySide = ""
marioLocationList = list()
rList = list()
eList = list()
bombScoreRatio = 0

myList = []
myList2 = []
xList = []
yList = []
tempList = []
temp2List = []
temp3List = []
temp4List = []
temp5List = []
locationList = []
# ... and assign them values coming form the input data file (filename)
readDataFileAndSetVariables(filename)

# Create a maze
theMaze = list()
theMaze = createMaze(theMaze, mazeWidth, mazeHeight, emptyCell)

# Create the boundary around the maze (not part of the maze)
hBoundary = list()
hBoundary = createBoundary(mazeWidth, boundary)

# Place treasures in the maze
rowIndex = 0
columnIndex = 1  
for obstacle in range(aNumOfTreasures):
    theMaze = placeInMaze(theMaze, int(rList[obstacle][rowIndex]), int(rList[obstacle][columnIndex]), treasure)

# Place bombs in the maze
for obstacle in range(aNumOfBombs):
    theMaze = placeInMaze(theMaze, int(eList[obstacle][rowIndex]), int(eList[obstacle][columnIndex]), bomb)

# Place Mario in the maze
theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), mario)
          
# Create exit gate and place it in the maze
# Place the exit gate at the opposite corner of Mario's location
exitGateLocationList = list()
hBoundary, exitGateLocationList = placeExitGate(mazeWidth, mazeHeight, int(marioLocationList[0][0]), int(marioLocationList[0][1]), hBoundary, exitGate)

# Set Mario's score
marioScore = setMarioScore(aNumOfBombs, bombScoreRatio)

    
# Part 2 - To be completed
# Here is the 'high-level' algorithm:

# As long as the player is playing ...

	# Display the maze
	# Once you have completed Part 1, uncomment the following Python statement and see what is displayed on the screen!
displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)

if marioScore == 0:
  print("Mario's score is now down to 0! You have lost!")

exitBool = False
breakBool = False
scoreBool = False

while marioScore != 0 and exitBool == False and scoreBool == False:
  
  print("\nMario's Score -> ", marioScore)

  if marioScore == 0:
    scoreBool == True
    break

  if marioLocationList[0] == exitGateLocationList and marioScore == 10:
    breakBool = True
    break

	# Display instructions to the player (see Sample Runs)
  instructions = input("\nMove Mario by entering the letter 'r' for right, 'l' for left, 'u' for up and 'd' for down, 'x' to exit the game: ").lower()

  if instructions == "r":
  #Move Right
    if marioScore == 0:
      scoreBool == True
      break


    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), emptyCell)
    marioLocationList[0][1] =  int(marioLocationList[0][1]+1)

    for y in range(0,len(eList)-1):
      if eList[y] == marioLocationList[0]:
        aNumOfBombs = aNumOfBombs - 1
        marioScore = marioScore - 1
        eList.remove(eList[y])
    
    for z in range(0, len(rList)-1):
      if rList[z] == marioLocationList[0]:
        aNumOfTreasures = aNumOfTreasures - 1
        marioScore = marioScore + 1
        rList.remove(rList[z])

    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), mario)
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)

  elif instructions == "l":
  #Move Left
    if marioScore == 0:
      scoreBool == True
      break

    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), emptyCell)
    marioLocationList[0][1] = int(marioLocationList[0][1]-1)

    for y in range(0,len(eList)-1):
      if eList[y] == marioLocationList[0]:
        aNumOfBombs = aNumOfBombs - 1
        marioScore = marioScore - 1
        eList.remove(eList[y])
    
    for z in range(0, len(rList)-1):
      if rList[z] == marioLocationList[0]:
        aNumOfTreasures = aNumOfTreasures - 1
        marioScore = marioScore + 1
        rList.remove(rList[z])
        
    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), mario)
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)

  elif instructions == "u":
  #Move Up

    if marioScore == 0:
      scoreBool == True
      break

    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), emptyCell)
    marioLocationList[0][0] = int(marioLocationList[0][0]-1)

    for y in range(0,len(eList)-1):
      if eList[y] == marioLocationList[0]:
        aNumOfBombs = aNumOfBombs - 1
        marioScore = marioScore - 1
        eList.remove(eList[y])
    
    for z in range(0, len(rList)-1):
      if rList[z] == marioLocationList[0]:
        aNumOfTreasures = aNumOfTreasures - 1
        marioScore = marioScore + 1
        rList.remove(rList[z])
        
    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), mario)
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)
  
  elif instructions == "d":
  #Move Down
    if marioScore == 0:
      scoreBool == True
      break
    
    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), emptyCell)
    marioLocationList[0][0] = int(marioLocationList[0][0]+1)

    for y in range(0,len(eList)-1):
      if eList[y] == marioLocationList[0]:
        aNumOfBombs = aNumOfBombs - 1
        marioScore = marioScore - 1
        eList.remove(eList[y])
    
    for z in range(0, len(rList)-1):
      if rList[z] == marioLocationList[0]:
        aNumOfTreasures = aNumOfTreasures - 1
        marioScore = marioScore + 1
        rList.remove(rList[z])
        
    theMaze = placeInMaze(theMaze, int(marioLocationList[0][0]), int(marioLocationList[0][1]), mario)
    displayMaze(theMaze, mazeWidth, mazeHeight, hBoundary, boundarySide)

  elif instructions == "x":
  #Exit Game
    exitBool = True
    print("\n-------")


if breakBool == True:
  print("\nMario has reached the exit gate with a score of 10! You win!")

if scoreBool == True:
  print("\nMario's score is now down to 0! You have lost!")


print("\n-------")

