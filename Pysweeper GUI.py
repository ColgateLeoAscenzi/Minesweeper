#Leo Ascenzi
#Colgate University

#Nota Bene: To fix error about Pysweeper instance not having atribute, put inside "class Pysweeper()"
#If you need self, from def __init__, pass self inside function (you need to do this if above statement is carried out"
#Otherwise self.Stuff should work

from Tkinter import *
import random
import time

class Pysweeper():
    def __init__(self, master):
        self.master = master
        self.WidthInput = StringVar()
        self.HeightInput = StringVar()
        self.MineInput = StringVar()
        
        def submit():
            global minenum
            #Grabs starter values
            w = int(self.WidthInput.get())
            h = int(self.HeightInput.get())
            minenum = int(self.MineInput.get())

            #Makes a list of mines
            mines = genmine(w,h,minenum)

            #Makes a board
            self.revealed = genrevealed(w,h)
            createboard(w,h,mines)
            self.GameStatusLabel.config(text = "Game In Progress")
   
                
        #Main Container
        self.MainContainer = Frame(master,
                                   width = 1920,
                                   height = 1080)
        self.MainContainer.pack(expand = YES,fill = BOTH)

        #Left Container with options
        self.LeftContainer = Frame(self.MainContainer,
                                   width = 320,
                                   bg = "white")
        self.LeftContainer.pack(side = LEFT,expand = YES,fill = BOTH)

        #Right container with game
        self.GameContainer = Frame(self.MainContainer,
                                   bg = "white")
        self.GameContainer.pack(side = RIGHT,expand = YES,fill = BOTH)

        
        #Width Entry
        self.WidthLabel = Label(self.LeftContainer,
                                text = "Width:",
                                bg = "white")
        self.WidthLabel.grid(row = 0, column = 0)
        
        self.WidthEntry = Entry(self.LeftContainer,
                                bg = "white",
                                exportselection = 0,
                                relief = RAISED,
                                textvariable = self.WidthInput)
        self.WidthEntry.grid(row = 0, column = 1)
        
        #Height Entry
        self.HeightLabel = Label(self.LeftContainer,
                                 text = "Height:",
                                 bg = "white")
        self.HeightLabel.grid(row = 1, column = 0)

        self.HeightEntry = Entry(self.LeftContainer,
                                 bg = "white",
                                 exportselection = 0,
                                 relief = RAISED,
                                 textvariable = self.HeightInput)
        self.HeightEntry.grid(row = 1, column = 1)

        #Mine Entry
        self.MineLabel = Label(self.LeftContainer,
                               text = "Mines:",
                               bg = "white")
        self.MineLabel.grid(row = 2, column = 0)
        
        self.MineEntry = Entry(self.LeftContainer,
                               bg = "white",
                               exportselection = 0,
                               relief = RAISED,
                               textvariable = self.MineInput)
        self.MineEntry.grid(row = 2, column = 1)

        #Submits the previous information

        self.SubmitButton = Button(self.LeftContainer,
                                   text = "Play!",
                                   command = submit)
        self.SubmitButton.grid(row = 3)

        #Game Status
        self.GameStatusLabel = Label(self.LeftContainer,
                                     bg = "white")
        self.GameStatusLabel.grid(row = 4)

        
        def genmine(w,h,minenum):
            #Initializes list and other variables
            minelist = []
            #Adds first mine and starts count with 1
            coord = [random.choice(range(w)),random.choice(range(h))]
            minelist += [coord]
            count = 1
            #Adds mines so long as they're below the number of specified mines
            while count < minenum:
                already = False
                coord = [random.choice(range(w)),random.choice(range(h))]
                for item in minelist:
                    if coord == item:
                        already = True
                if not already:
                    minelist += [coord]
                    count += 1

            return minelist
        
        def genrevealed(width,height):
            '''(int, int) -> (lst)
            Creates a list of False
            to count as the revealed
            '''
            #Same creating method as genboard
            board = []
            for h in range(width):
                temprow = []
                for w in range(height):
                    temprow += [False]
                board += [temprow]
            
            return board
        
        
        
        def createboard(x,y,mines):
            global board
            #OLD GENBOARD
            board = []
            for h in range(x):
                #For every width
                temprow = []
                for w in range(y):
                    #Add to a temporary row
                    temprow += ["[ ]"]
                board += [temprow]
                
                
            #OLD ADDMINES
            for item in mines:
                board[int(item[0])][int(item[1])] = "[*]"
                
            #Set Zeros
            for j in range(x):
                for i in range(y):
                    #i,j
                    #0,0 -> 1,0 -> 2,0
                    if board[j][i] == "[*]":
                        #Top Left
                        if j != 0 and i != 0:
                            if board[j-1][i-1] != "[*]":
                                board[j-1][i-1] = [0]
                        #Top Mid
                        if j != 0:
                            if board[j-1][i] != "[*]":
                                board[j-1][i] = [0]
                        #Top Right
                        if j != 0 and i != y-1:
                            if board[j-1][i+1] != "[*]":
                                board[j-1][i+1] = [0]
                        #Mid Left
                        if i != 0:
                            if board[j][i-1] != "[*]":
                                board[j][i-1] = [0]
                        #Mid Right
                        if i != y-1:
                            if board[j][i+1] != "[*]":
                                board[j][i+1] = [0]
                        #Bot Left
                        if j != x-1 and i != 0:
                            if board[j+1][i-1] != "[*]":
                                board[j+1][i-1] = [0]
                        #Bot Mid
                        if j != x-1:
                            if board[j+1][i] != "[*]":
                                board[j+1][i] = [0]
                        #Bot Mid
                        if j != x-1 and i != y-1:
                            if board[j+1][i+1] != "[*]":
                                board[j+1][i+1] = [0]
            #Add Mines
            for j in range(x):
                for i in range(y):
                    #i,j
                    #0,0 -> 1,0 -> 2,0
                    if board[j][i] == "[*]":
                        #Top Left
                        if j != 0 and i != 0:
                            if board[j-1][i-1] != "[*]":
                                board[j-1][i-1][0] += 1
                        #Top Mid
                        if j != 0:
                            if board[j-1][i] != "[*]":
                                board[j-1][i][0] += 1
                        #Top Right
                        if j != 0 and i != y-1:
                            if board[j-1][i+1] != "[*]":
                                board[j-1][i+1][0] += 1
                        #Mid Left
                        if i != 0:
                            if board[j][i-1] != "[*]":
                                board[j][i-1][0] += 1
                        #Mid Right
                        if i != y-1:
                            if board[j][i+1] != "[*]":
                                board[j][i+1][0] += 1
                        #Bot Left
                        if j != x-1 and i != 0:
                            if board[j+1][i-1] != "[*]":
                                board[j+1][i-1][0] += 1
                        #Bot Mid
                        if j != x-1:
                            if board[j+1][i] != "[*]":
                                board[j+1][i][0] += 1
                        #Bot Mid
                        if j != x-1 and i != y-1:
                            if board[j+1][i+1] != "[*]":
                                board[j+1][i+1][0] += 1
            for j in range(x):
                for i in range(y):
                    if board[j][i][0] == "[":
                        if board[j][i][1] == "*":
                            #Creates mine buttons
                            self.button = Button(self.GameContainer,
                                                 bg = "gray77",
                                                 fg = "gray77",
                                                 activebackground ="gray77",
                                                 activeforeground = "gray77",
                                                 width = 2,
                                                 height = 1,
                                                 text = "*",
                                                 textvar = str(j)+"."+str(i))
                            self.button['command'] = lambda binst = self.button: self.explode(binst)
                            self.button.grid(row = j, column = i)
                        else:
                            #Otherwise creates a normal button with no number
                            self.button = Button(self.GameContainer,
                                                 bg = "gray77",
                                                 fg = "gray77",
                                                 activebackground = "gray77",
                                                 activeforeground = "gray77",
                                                 width = 2,
                                                 height = 1,
                                                 textvar = str(j)+"."+str(i))
                            self.button['command'] = lambda binst = self.button: self.click(binst)
                            self.button.grid(row = j, column = i)

                    else:
                        #Or creates a button with a number
                        self.button = Button(self.GameContainer,
                                             bg = "gray77",
                                             fg = "gray77",
                                             #Makes sure there's no cheating by selecting buttons
                                             activebackground = "gray77",
                                             activeforeground = "gray77",
                                             width = 2,
                                             height = 1,
                                             text = board[j][i][0],
                                             textvar = str(j)+"."+str(i))
                        self.button['command'] = lambda binst = self.button: self.click(binst)
                        self.button.grid(row = j, column = i)
                        
                              

    def updateboard(self,w,h,revealed):
            #This loops checks each button and updates them
            for button in self.GameContainer.winfo_children():
                #Converts the widgets textvar into text, splits it, indexes it and then makes it an int
                if str(button.cget("text")) != "*":
                    x = int(str(button.cget("textvar")).split(".")[0])
                    y = int(str(button.cget("textvar")).split(".")[1])
                    if revealed[x][y] == True:
                        if str(button.cget("text")).isdigit():
                            if int(str(button.cget("text"))) == 1:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "blue")
                            elif int(str(button.cget("text"))) == 2:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "dark green")
                            elif int(str(button.cget("text"))) == 3:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "red")
                            elif int(str(button.cget("text"))) == 4:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "dark blue")
                            elif int(str(button.cget("text"))) == 5:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "orangered")
                            elif int(str(button.cget("text"))) == 6:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "teal")
                            elif int(str(button.cget("text"))) == 7:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "black")
                            elif int(str(button.cget("text"))) == 8:
                                button.config(state = DISABLED,relief = FLAT, disabledforeground = "gray60")
                        else:
                            button.config(state = DISABLED,relief = FLAT)


    def win(self):
        i = 0
        for item in self.GameContainer.winfo_children():
            if item.cget("state") == DISABLED:
                i += 1
            
        if i == (int(self.WidthInput.get())*int(self.HeightInput.get()))-minenum:
            for button in self.GameContainer.winfo_children():
                if str(button.cget("text")) == "*":
                    button.config(state = DISABLED,
                                  disabledforeground = "gray76")
            self.GameStatusLabel.config(text = "Game Won!",
                                        fg = "green")
            root.update()
                    
        
    def click(self, binst):
        y = int(str(binst.cget("textvar")).split(".")[0])
        x = int(str(binst.cget("textvar")).split(".")[1])
        clickw = int(self.WidthInput.get())
        clickh = int(self.HeightInput.get())
        if self.revealed[y][x] == False and not str(board[y][x][0]).isdigit():
            self.revealed[y][x] = True
            self.cascadeall(clickh,clickw,x,y,board,self.revealed)

        #If it is a number it doesn't cascade
        elif self.revealed[y][x] == False:
            self.revealed[y][x] = True


        binst.config(state = DISABLED,relief = FLAT)
        
        self.updateboard(x,y,self.revealed)
        self.win()

    def cascadeall(self,w,h,x,y,board,revealed):
        #Right
        #Recurses if there is no digit and it isn't revealed
        if x != w-1 and revealed[y][x+1]!= True and not str(board[y][x+1][0]).isdigit():
            revealed[y][x+1] = True
            self.cascadeall(w,h,x+1,y,board,revealed)
        #Does not recurse if it is a digit
        if x != w-1 and revealed[y][x+1]!= True and str(board[y][x+1][0]).isdigit():
            revealed[y][x+1] = True
            

        #Down
        #Recurses if there is no digit and it isn't revealed
        if y != h-1 and revealed[y+1][x] != True and not str(board[y+1][x][0]).isdigit():
            revealed[y+1][x] = True
            self.cascadeall(w,h,x,y+1,board,revealed)
        #Does not recurse if it is a digit
        if y != h-1 and revealed[y+1][x] != True and str(board[y+1][x][0]).isdigit():
            revealed[y+1][x] = True

        #Left
        #Recurses if there is no digit and it isn't revealed
        if x != 0 and revealed[y][x-1] != True and not str(board[y][x-1][0]).isdigit():
            revealed[y][x-1] = True
            self.cascadeall(w,h,x-1,y,board,revealed)
        #Does not recurse if it is a digit
        if x != 0 and revealed[y][x-1] != True and str(board[y][x-1][0]).isdigit():
            revealed[y][x-1] = True

        #Up
        #Recurses if there is no digit and it isn't revealed
        if y != 0 and revealed[y-1][x] != True and not str(board[y-1][x][0]).isdigit():
            revealed[y-1][x] = True
            self.cascadeall(w,h,x,y-1,board,revealed)
        #Does not recurse if it is a digit
        if y != 0 and revealed[y-1][x] != True and str(board[y-1][x][0]).isdigit():
            revealed[y-1][x] = True

        
    def explode(self, binst):
        for button in self.GameContainer.winfo_children():
            if str(button.cget("text")).isdigit():
                if int(str(button.cget("text"))) == 1:
                    button.config(state = DISABLED, disabledforeground = "blue")
                elif int(str(button.cget("text"))) == 2:
                    button.config(state = DISABLED, disabledforeground = "dark green")
                elif int(str(button.cget("text"))) == 3:
                    button.config(state = DISABLED, disabledforeground = "red")
                elif int(str(button.cget("text"))) == 4:
                    button.config(state = DISABLED, disabledforeground = "dark blue")
                elif int(str(button.cget("text"))) == 5:
                    button.config(state = DISABLED, disabledforeground = "orangered")
                elif int(str(button.cget("text"))) == 6:
                    button.config(state = DISABLED, disabledforeground = "teal")
                elif int(str(button.cget("text"))) == 7:
                    button.config(state = DISABLED, disabledforeground = "black")
                elif int(str(button.cget("text"))) == 8:
                    button.config(state = DISABLED, disabledforeground = "gray60")
            elif str(button.cget("text")) == "*":
                button.config(state = DISABLED,disabledforeground= "black")
            else:
                button.config(state = DISABLED)
    
        for button in self.GameContainer.winfo_children():
            button.config(background = random.choice(["red","orange"]))
            self.GameStatusLabel.config(text = "Game Lost!",
                                        fg = "red")
            
        root.update()

    
    
                


if __name__=='__main__':
    root = Tk()
    root.title("Pysweeper v1 by Leo Ascenzi")
    PysweeperApp = Pysweeper(root)
    root.mainloop()
