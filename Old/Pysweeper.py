#Leo Ascenzi
#Colgate University


import random
import time

def genboard(width,height):
    '''(int, int) -> (lst)
    Creates a board of specified
    width and height
    '''
    board = []
    for w in range(width):
        #For every width
        temprow = []
        for h in range(height):
            #Add to a temporary row
            temprow += ["[ ]"]
        board += [temprow]
    
    return board

def genrevealed(width,height):
    '''(int, int) -> (lst)
    Creates a list of False
    to count as the revealed
    '''
    #Same creating method as genboard
    board = []
    for w in range(width):
        temprow = []
        for h in range(height):
            temprow += [False]
        board += [temprow]
    
    return board

def genallrevealed(width,height):
    '''(int, int) -> (lst)
    Creates a list of True
    so that when a player
    loses the whole board is
    revealed
    '''
    #Same creation method as genboard
    board = []
    for w in range(width):
        temprow = []
        for h in range(height):
            temprow += [True]
        board += [temprow]
    
    return board


def displayboard(w,h,board,revealed):
    '''(int, int, list, list) -> (prints)
    Takes the width and height of the board
    and the actual board and what is revealed
    and displays the board to the user
    '''
    #Sets up the top of the display
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    testdisplay = "   "
    for x in range(w):
        testdisplay += " "+alphabet[x]+" "
    testdisplay += "\n"

    #Adds the actual board
    for i in range(w):
        #For every row, adds at the start the number
        if i < 9:
            testdisplay += str(i+1)+"  "
        else:
            testdisplay += str(i+1)+" "
            
        for j in range(h):
            #For every column, if it's revealed, it shows the actual board
            if revealed[i][j] == True:
                testdisplay += str(board[i][j])
            #if not it displays the unclicked sign
            else:
                testdisplay += "[+]"
        testdisplay += "\n"
    print testdisplay

def click(w,h,board,revealed,minenum):
    '''(int, int, list, list, int) -> (str)
    Checks if the area clicked is a minenum,
    or if the amount of revealed tiles leaves
    the only option for unrevealed tiles
    as mines, meaning a win
    '''
    condition = ""
    x,y = getclick(w,h,revealed,board)
    
    #You Lose if you click on a mine
    if revealed[y][x] == True and board[y][x] == "[*]":
        condition = "loss"
        return condition

    #Win if the number of unrevealed tiles is the number of mines
    if w*h - countrevealed(w,h,revealed) == minenum:
        condition = "win"
        return condition
    

def getclick(w,h,revealed,board):
    '''(int, int, list, list) -> (str, int)
    Takes the input of a click and continues
    to ask until it's an acceptable coordinate
    then it cascades the board on that click
    and then gives back the place the user clicked
    '''
    while True:
        while True:
            while True:
                #First checks if it's valid input
                xy = raw_input("Enter a coordinate to click (letter,number): ").split(",")
                if len(xy) != 2:
                    print "Invalid Input: Invalid Dimensions"
                else:
                    break

            x = xy[0].lower()
            y = xy[1]
            
            if not x.isalpha():
                print "Invalid Input: X Coordinate Must Be A Letter"
                print
            elif not y.isdigit():
                print "Invalid Input: Y Coordinate Must Be A Number"
                print
            elif int(y)>h:
                print "Invalid Input: Y Is Too Big"
                print
            elif int(y)<1:
                print "Invalid Input: Y Is Too Small"
                print
            else:
                break

        #Then Checks and Reveals the Tile

        #Converts them into the coordinates
        x = ord(x)-97
        y = int(y)-1

        #Checks if the board hasn't been clicked on, and it's not a number
        if revealed[y][x] == False and not str(board[y][x][0]).isdigit():
            revealed[y][x] = True
            #Cascades the clicks if this is true
            cascadeall(w,h,x,y,board,revealed)

            break

        #If it is a number it doesn't cascade
        elif revealed[y][x] == False:
            revealed[y][x] = True

            break

        #If it's already clicked on, tell the user                                    
        elif revealed[y][x] == True:
            print "You've already clicked here!"
            print
            
    return x,y



def cascadeall(w,h,x,y,board,revealed):
    '''(int, int, int, int, lst, lst) -> (modifies a list)
    Takes the board and revealed, and length and width
    then clicks on the x and y coordinates and continues
    to recurse until the base case is triggered
    '''
    #Right
    #Recurses if there is no digit and it isn't revealed
    if x != w-1 and revealed[y][x+1]!= True and not str(board[y][x+1][0]).isdigit():
        revealed[y][x+1] = True
        cascadeall(w,h,x+1,y,board,revealed)
    #Does not recurse if it is a digit
    if x != w-1 and revealed[y][x+1]!= True and str(board[y][x+1][0]).isdigit():
        revealed[y][x+1] = True
        

    #Down
    #Recurses if there is no digit and it isn't revealed
    if y != h-1 and revealed[y+1][x] != True and not str(board[y+1][x][0]).isdigit():
        revealed[y+1][x] = True
        cascadeall(w,h,x,y+1,board,revealed)
    #Does not recurse if it is a digit
    if y != h-1 and revealed[y+1][x] != True and str(board[y+1][x][0]).isdigit():
        revealed[y+1][x] = True

    #Left
    #Recurses if there is no digit and it isn't revealed
    if x != 0 and revealed[y][x-1] != True and not str(board[y][x-1][0]).isdigit():
        revealed[y][x-1] = True
        cascadeall(w,h,x-1,y,board,revealed)
    #Does not recurse if it is a digit
    if x != 0 and revealed[y][x-1] != True and str(board[y][x-1][0]).isdigit():
        revealed[y][x-1] = True

    #Up
    #Recurses if there is no digit and it isn't revealed
    if y != 0 and revealed[y-1][x] != True and not str(board[y-1][x][0]).isdigit():
        revealed[y-1][x] = True
        cascadeall(w,h,x,y-1,board,revealed)
    #Does not recurse if it is a digit
    if y != 0 and revealed[y-1][x] != True and str(board[y-1][x][0]).isdigit():
        revealed[y-1][x] = True

        
def countrevealed(w,h,revealed):
    '''(int, int, lst) -> (int)
    Takes the width, height and board
    and returns the number of tiles
    that are revealed
    '''

    #Counts the number of revealed ones
    count = 0
    for i in range(w):
        for j in range(h):
            if revealed[i][j] == True:
                count += 1

    return count

def genmine(w,h,minenum):
    minelist = []
    x = range(w)
    y = range(h)
    randx = str(random.choice(x))
    randy = str(random.choice(y))
    coord = [randx,randy]
    minelist += [coord]
    count = 1
    while count < minenum:
        already = False
        randx = str(random.choice(x))
        randy = str(random.choice(y))
        coord = [randx, randy]
        for item in minelist:
            if coord == item:
                already = True
        if not already:
            minelist += [coord]
            count += 1

    return minelist

def addmines(board,mine):
    for item in mine:
        board[int(item[0])][int(item[1])] = "[*]"

    return board

def getdimensions():
    '''(None) -> (int, int)
    Continues to ask user for
    dimensions of the board
    until the conditions are met
    '''
    #Conditions: only 2 coords, alphabetic x, numeric y, can't go out of the length of the alphabet
    while True:
        while True:
            wh = raw_input("Please enter board dimensions seperated by an 'x': ").split("x")
            if len(wh) != 2:
                print "Invalid Input: Invalid Dimensions"
            else:
                break
        w = wh[0]
        h = wh[1]
        if w.isalpha():
            print "Invalid Input: Width cannot be alphabetic!"
            print
        elif h.isalpha():
            print "Invalid Input: Height cannot be alphabetic!"
            print
        elif int(w)<1:
            print "Invalid Input: Width cannot be less than 0!"
            print
        elif int(h)<1:
            print "Invalid Input: Height cannot be less than 0!"
            print
        elif int(w)>26:
            print "Invalid Input: Width cannot be greater than 26!"
            print
        elif int(h)>26:
            print "Invalid Input: Height cannot be greater than 26!"
            print

        else:
            return w,h

def getminenum(w,h):
    '''(int, int) -> (int)
    Within the bounds of
    the total area which is
    w*h, creates collects
    and acceptable number of
    mines to add
    '''
    while True:
        minenum = raw_input("Enter a number of mines! ")
        charcount = 0
        for char in minenum:
            if char.isalpha():
                charcount += 1
                
        if charcount > 0:
            print "Invalid Input: Minenum Must Be A Number!"
            print
        elif int(minenum) > w*h:
            print "Invalid Input: More Mines Than Tiles!"
            print
        elif int(minenum) < 1:
            print "Invalid Input: Not Enough Mines!"
            print
        else:
            return int(minenum)



def setthezeros(w,h,board):
    '''
    Adds 0's to the board
    around the positions of
    the mines so they can
    be added to later
    '''
    checktopleft0(w,h,board)
    checktopmid0(w,h,board)
    checktopright0(w,h,board)

    checkmidleft0(w,h,board)
    checkmidright0(w,h,board)

    checkbotleft0(w,h,board)
    checkbotmid0(w,h,board)
    checkbotright0(w,h,board)

def setthemines(w,h,board):
    '''
    Adds numbers to the zeros
    which were previously added
    for every mine square
    all adjascent squares are
    increased by 1
    '''
    checktopleft(w,h,board)
    checktopmid(w,h,board)
    checktopright(w,h,board)

    checkmidleft(w,h,board)
    checkmidright(w,h,board)

    checkbotleft(w,h,board)
    checkbotmid(w,h,board)
    checkbotright(w,h,board)

    

#Sets the area around the mines to zero
#Only if the area around the mine is not
#out of bounds or anything
def checktopleft0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != 0 and j != 0:
                    if board[i-1][j-1] != "[*]":
                        board[i-1][j-1] = [0]
def checktopmid0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != 0:
                    if board[i-1][j] != "[*]":
                        board[i-1][j] = [0]
def checktopright0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != 0 and j != w-1:
                    if board[i-1][j+1] != "[*]":
                        board[i-1][j+1] = [0]
def checkmidleft0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if j != 0:
                    if board[i][j-1] != "[*]":
                        board[i][j-1] = [0]
def checkmidright0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if j != w-1:
                    if board[i][j+1] != "[*]":
                        board[i][j+1] = [0]
def checkbotleft0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != h-1 and j != 0:
                    if board[i+1][j-1] != "[*]":
                        board[i+1][j-1] = [0]
def checkbotmid0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != h-1:
                    if board[i+1][j] != "[*]":
                        board[i+1][j] = [0]
def checkbotright0(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != w-1 and j != h-1:
                    if board[i+1][j+1] != "[*]":
                        board[i+1][j+1] = [0]
#Adds 1 to the area around the mines
#Only if the area around the mine is not
#out of bounds or anything
def checktopleft(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != 0 and j != 0:
                    if board[i-1][j-1] != "[*]":
                        board[i-1][j-1][0] += 1
def checktopmid(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != 0:
                    if board[i-1][j] != "[*]":
                        board[i-1][j][0] += 1
def checktopright(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != 0 and j != w-1:
                    if board[i-1][j+1] != "[*]":
                        board[i-1][j+1][0] += 1
def checkmidleft(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if j != 0:
                    if board[i][j-1] != "[*]":
                        board[i][j-1][0] += 1
def checkmidright(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if j != w-1:
                    if board[i][j+1] != "[*]":
                        board[i][j+1][0] += 1
def checkbotleft(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != h-1 and j != 0:
                    if board[i+1][j-1] != "[*]":
                        board[i+1][j-1][0] += 1
def checkbotmid(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != h-1:
                    if board[i+1][j] != "[*]":
                        board[i+1][j][0] += 1
def checkbotright(w,h,board):
    for i in range(w):
        for j in range(h):
            if board[i][j] == "[*]":
                if i != w-1 and j != h-1:
                    if board[i+1][j+1] != "[*]":
                        board[i+1][j+1][0] += 1
#End of wall of repetitive text

def playgame():
    '''(None) -> (None)
    Plays the game and
    continues to play
    the game until the
    user decides they don't
    want to
    '''
    while True:
        singlegame()
        ans = raw_input("Would you like to try again? ")
        if ans.lower() in "no":
            print "Okay byeee!!!"
            break
        print

def displayrules():
    print "Rules:"
    print "Click on tiles to reveal them"
    print "Reveal all the tiles that aren't mines to win"
    print "Reveal a mine to lose"
    print
    time.sleep(0.5)
    print "A number tile indicates that there is 'x' number"
    print "of mines next to it (NESW,NE,NW,SE,SW)"
    print
    time.sleep(0.5)
    print "In order to click, simple enter a letter and"
    print "a number seperated by a comma."
    print "The letter and number should correspond to the"
    print "coordinate grid that is displayed"
    print
    time.sleep(0.5)
    print "These messages will not appear the next time you"
    print "run this program. If you want to see these messages"
    print "again, simply delete the config file in this folder."
    print
    time.sleep(0.5)
    print "Enjoy!"
    print
    time.sleep(0.5)
    
    
def singlegame():
    '''(None) -> (None)
    Sets up the board for
    one game
    '''
    #Sets up first play
    print "Welcome to PySweeper v.1!"

    setup = open("config.txt","a")
    setup.close()
    
    config = open("config.txt","r+")
    if "1" not in config.readline():
        ans = raw_input("Have you played PySweeper before? ").lower()
        if ans in "yes":
            config = open("config.txt","w")
            config.write("1")
            config.close()

        else:
            config = open("config.txt","w")
            config.write("1")
            config.close()
            displayrules()
                
    #Sets up dimensions
    w,h = getdimensions()
    w = int(w)
    h = int(h)

    #Generates Revealed
    revealed = genrevealed(w,h)

    #Incase you lose
    allrevealed = genallrevealed(w,h)

    #Generates Board
    board = genboard(w,h)

    #Gets the number of mines
    minenum = getminenum(w,h)

    #Generates the mines
    mine = genmine(w,h,minenum)

    #Adds the mines
    board = addmines(board,mine)
    
    #Add the zeros
    setthezeros(w,h,board)

    #Add the mines

    setthemines(w,h,board)
    
    displayboard(w,h,board,revealed)

##    #XRAY
##    displayboard(w,h,board,allrevealed)

    while True:
            
        condition = click(w,h,board,revealed,minenum)
        displayboard(w,h,board,revealed)

        
        if condition == "loss":
            print "KA-BOOOOOOOOOOM!!!!"
            print
            displayboard(w,h,board,allrevealed)
            print
            print "You Lose!!!"
            print
            break
        elif condition == "win":
            print "You didn't hit a mine!"
            print "You Win!!!"
            print
            break

playgame()

