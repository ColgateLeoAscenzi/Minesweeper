#Leo Ascenzi
#Minesweeper Game v2

#NOW GOING TO MESS WITH CLICK

import random

def genboard(width,height):
    board = []
    for w in range(width):
        temprow = []
        for h in range(height):
            temprow += ["[ ]"]
        board += [temprow]
    
    return board

def genrevealed(width,height):
    board = []
    for w in range(width):
        temprow = []
        for h in range(height):
            temprow += [False]
        board += [temprow]
    
    return board

def genallrevealed(width,height):
    board = []
    for w in range(width):
        temprow = []
        for h in range(height):
            temprow += [True]
        board += [temprow]
    
    return board


def displayboard(w,h,board,revealed):

    testdisplay = ""
    for i in range(w):
        for j in range(h):
            if revealed[i][j] == True:
                testdisplay += str(board[i][j])
            else:
                testdisplay += "[+]"
        testdisplay += "\n"
    print testdisplay

def click(w,h,board,revealed,minenum):

    condition = ""
    x,y = getclick(w,h,revealed,board)
    
    #You Lose if you click on a mine
    if revealed[y][x] == True and board[y][x] == "[*]":
        print "clicked on mine"
        condition = "loss"
        return condition

    if w*h - countrevealed(w,h,revealed) == minenum:
        condition = "win"
        return condition
    

def getclick(w,h,revealed,board):

    while True:
        while True:
            while True:
                #First checks if it's valid input
                xy = raw_input("Enter a coordinate to click (x,y): ").split(",")
                if len(xy) != 2:
                    print "Invalid Input: This is not 3D"
                    print
                else:
                    break

            x = xy[0]
            y = xy[1]
            
            if not x.isdigit():
                print "Invalid Input: X Coordinate Must Be A Number"
                print
            elif not y.isdigit():
                print "Invalid Input: Y Coordinate Must Be A Number"
                print
            elif int(x)>w-1:
                print "Invalid Input: X Is Too Big"
                print
            elif int(x)<0:
                print "Invalid Input: X Is Too Small"
                print
            elif int(y)>h-1:
                print "Invalid Input: Y Is Too Big"
                print
            elif int(y)<0:
                print "Invalid Input: Y Is Too Small"
                print
            else:
                break

        #Then Checks and Reveals the Tile
        x = int(x)
        y = int(y)
        if revealed[y][x] == False:
            revealed[y][x] = True
            
            
            print "You clicked on coordinate: ("+str(x)+","+str(y)+")"
            print
            
            #Does the Initial Cascade
            cascadeall(w,h,x,y,board,revealed)

            #Recursion
            #or for loop
            for i in range(w):
                for j in range(h):
                    if revealed[i][j] == True:
                        cascadeall(w,h,i,j,board,revealed)



            break
        elif revealed[y][x] == True:
            print "You've already clicked here!"
            print

    return x,y

def cascadeall(w,h,x,y,board,revealed):
    cascaderight(w,h,x,y,board,revealed)
    cascadedown(w,h,x,y,board,revealed)
    cascadeup(w,h,x,y,board,revealed)
    cascadeleft(w,h,x,y,board,revealed)

def cascaderight(w,h,x,y,board,revealed):

    #As if it's revealed, then you no longer cascade.
    #Right
    while True:
        if str(board[y][x])[1].isdigit() or board[y][x] == "[*]":
            break
        revealed[y][x] = True
        if x == w-1:
            break
        x += 1

def cascadedown(w,h,x,y,board,revealed):
    #Down
    while True:
        if str(board[y][x])[1].isdigit() or board[y][x] == "[*]":
            break
        revealed[y][x] = True
        if y == h-1:
            break
        y += 1



def cascadeleft(w,h,x,y,board,revealed):
    #Left
    while True:
        if str(board[y][x])[1].isdigit() or board[y][x] == "[*]":
            break
        revealed[y][x] = True
        if x == 0:
            break
        x -= 1


def cascadeup(w,h,x,y,board,revealed):
    #Up
    while True:
        if str(board[y][x])[1].isdigit() or board[y][x] == "[*]":
            break
        revealed[y][x] = True
        if y == 0:
            break
        y -= 1

        
def countrevealed(w,h,revealed):

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
    coord = randx + randy
    minelist += [coord]
    count = 1
    while count < minenum:
        already = False
        randx = str(random.choice(x))
        randy = str(random.choice(y))
        coord = randx + randy
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
    while True:
        while True:
            wh = raw_input("Please enter board dimensions seperated by an 'x': ").split("x")
            if len(wh) != 2:
                print "Invalid Input: This is not 3D!"
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
    checktopleft0(w,h,board)
    checktopmid0(w,h,board)
    checktopright0(w,h,board)

    checkmidleft0(w,h,board)
    checkmidright0(w,h,board)

    checkbotleft0(w,h,board)
    checkbotmid0(w,h,board)
    checkbotright0(w,h,board)

def setthemines(w,h,board):
    checktopleft(w,h,board)
    checktopmid(w,h,board)
    checktopright(w,h,board)

    checkmidleft(w,h,board)
    checkmidright(w,h,board)

    checkbotleft(w,h,board)
    checkbotmid(w,h,board)
    checkbotright(w,h,board)
    
        

#SETS THEM TO ZEEEEEEEEEEEEEEEEEROOOOOOOOOOOOOOOOOOOOO
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
#ADDS THE MINESSSSSSSSSSSSSSSSSSSS


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
#YEAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH

def playgame():
    while True:
        singlegame()
        ans = raw_input("Would you like to try again? ")
        if ans.lower() in "no":
            print "Okay byeee!!!"
            break
        print
    
def singlegame():
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

    #XRAY
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

