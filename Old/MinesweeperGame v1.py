#Leo Ascenzi
#Minesweeper Text Edition v1
import random

def game():
    #Prints rules
    yesorno = raw_input("Do you know the rules? ")
    if yesorno.lower() in "no":
        rules()

    #Gets dimensions
    w,h,minenum = get_dimensions()

    #Generates mine positions
    mines = generate_minecoords(w,h,minenum)

    #Makes an empty board then populates it
    emptyboard = generate_emptyboard(w,h)
    unclickedboard = add_unclickedcells(w,h,emptyboard)
    coordinatedboard = add_coordinates(w,h,unclickedboard)
    print "This is what the board will look like"
    displayboard = display_board(coordinatedboard)
    print
    print "This is what it actually is"
    print coordinatedboard
    print "Mines:",mines
    
##    fullboard = add_mines(w,h,coordinatedboard,mines)

def get_dimensions():
    while True:
        #Gathers dimension input
        wh = raw_input("Enter the dimensions of your game board seperated by an 'x' (26x26 max): ")
        w = int((wh.split("x"))[0])
        h = int((wh.split("x"))[1])

        #Keeps asking until the dimensions aren't above 25x25 or below 0x0
        if w < 27 and h < 27:
            if w > 0 and h > 0:
                break
            else:
                print "You must have dimensions greater than 1x1"
                print
        else:
            print "Your dimensions cannot exceed 26x26"
            print
            
    while True:
        #Gathers the number of mines
        minenum = int(raw_input("Enter the number of mines for this game: "))

        #Keeps asking until the number of mines doesn't exceed the number of squares
        if minenum < 0:
            minenum = 1

        if minenum < (w*h + 1):
            break
        else:
            print "You have more mines than spaces in the board!"
            print

    return (w,h,minenum)
    
    
def rules():
    #Prints the rules
    print "Placeholder text here"

def generate_minecoords(w,h,minenum):
    #Sets up the start thing
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    #Sets up a list for the coordinates
    minelist = []

    #Generates coordinates until there are enough mines
    totalmines = 0

    #Messy but works
    while totalmines < minenum:
        for i in range(h):
            tempbet = random.randint(0,h-1)
            tempnum = (random.randint(0,w-1)+1)
            while alphabet[tempbet]+str(tempnum) not in minelist and totalmines < minenum:
                minelist += [alphabet[tempbet]+str(tempnum)]
                totalmines += 1
                
    return minelist

def generate_emptyboard(w,h):
    #Makes rows
    emptyboard = []
    for i in range(h):
        for j in range(w):
            emptyboard += [[[],[],[]]]
        emptyboard += ["ENDROW"]
    
    return emptyboard

def add_unclickedcells(w,h,board):
    #Allows row skipping
    skipfactor = 0
    #Cycles first through the rows
    for i in range(h):
        i = 0
        #If it is endrow then make the row skipping factor
        while True:
            if board[(i+skipfactor)] == "ENDROW":
                skipfactor += w + 1
                break
            #Otherwise add the symbol for unclicked
            else:
                board[(i+skipfactor)][0] = ["+"]
                i += 1
        

    return board

def add_coordinates(w,h,board):
    coordlist = []
    #Add the letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    skipfactor = 0
    overalli = 0
    for i in range(h):
        i = 0
        while True:
            if board[(i+skipfactor)] == "ENDROW":
                skipfactor += w + 1
                #Only updates letter after every row
                overalli += 1
                break
            else:
                board[(i+skipfactor)][1] =  [alphabet[overalli]]
                i += 1


    #Adds the numbers
    skipfactor = 0
    for i in range(h):
        i = 0
        while True:
            if board[(i+skipfactor)] == "ENDROW":
                skipfactor += w + 1
                break
            else:
                board[(i+skipfactor)][1] = [str(board[(i+skipfactor)][1])[2:3]+str(i+1)]
                i += 1


    return board

def display_board(board):
    display = ""
    for item in board:
        if item == "ENDROW":
            display += "\n"

        else:
            display += item[0][0]
            

    print display
        

##def add_mines(w,h,board,mines):
##    minesadded = 0
##    while minesadded < mines:

