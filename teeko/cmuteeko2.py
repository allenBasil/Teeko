
import pip
import tkinter as tk 
import turtle
from cmu_graphics import * 



def drawWindow():
    # makes an empty board full of zeros
    board = [[0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]]
    # pattern to follow ot make board
    checkerboard = [[1,0,1,0,1], 
         [0,1,0,1,0],
         [1,0,1,0,1], 
         [0,1,0,1,0], 
         [1,0,1,0,1]] 
    
    # sets the app background to white 
    app.backgroud=rgb(31,31,31)
    # makes the checkerboard pattern
    for i in range(5):
        
        for j in range(5):
            
            if checkerboard[i][j]==0:
                color = 'white'
            else:
                color = 'black'
        

            Square = Rect(100+j*40,100+i*40, 40, 40, fill =color ,borderWidth= 2, border = 'black' ) 
             
             
            board[i][j]=Square
        

   # returns the board which is rectangles
    return(board)



def getBoardCoord(square):
    # goes through each row and checks if the square that is pass is in the row, then returns the row and colum of the square in relation to the board
    ''' checks if the given argument is in a list called board'''
    for row in board:
        if square in row  :
            return(board.index(row),row.index(square))
            
def isemptySpace(square):
    '''' checks if the given argument doesn't contain any other shape '''
    for i in range(4):
        if square.containsShape(blueP[i])==True or square.containsShape(redP[i])==True:
            
            return False
    return(True)

def validMoves(square):
    
    row, col = getBoardCoord(square)
    possibleMoves=[]
    validMoves = []
    # goes through every row for the given square and makes the list PossibleMoves which has all possible moves which are one away from the 
    if row ==0 :
        if col==0:
            possibleMoves = [board[row+1][col],board[row][col+1],board[row+1][col+1]]
        elif col in [1,2,3]:
            possibleMoves = [board[row][col+1],board[row][col-1], board[row+1][col-1],board[row+1][col+1],board[row+1][col]]
        elif col== 4:
            possibleMoves = [board[row+1][col],board[row][col-1],board[row+1][col-1]]
    if row in [1,2,3]:
        if col==0:
            possibleMoves = [board[row+1][col],board[row-1][col],board[row-1][col+1],board[row+1][col+1],board[row][col+1]]
        elif col in [1,2,3]:
            possibleMoves = [board[row-1][col-1],board[row-1][col],board[row-1][col+1],
                             board[row][col-1],board[row][col+1],
                             board[row+1][col-1],board[row+1][col],board[row+1][col+1]]
        elif col ==4:
            possibleMoves = [board[row-1][col],board[row+1][col],board[row-1][col-1],board[row+1][col-1],board[row][col-1]]
    if row ==4:
        if col ==0:
            possibleMoves = [board[row-1][col],board[row][col+1],board[row-1][col+1]]
        elif col in [1,2,3]:
            possibleMoves = [board[row-1][col],board[row][col-1], board[row][col+1],board[row-1][col+1],board[row-1][col-1]]
        elif col == 4:
            possibleMoves = [board[row-1][col],board[row][col-1],board[row-1][col-1]]
    for i in possibleMoves:
        if isemptySpace(i)==True:
            validMoves.append(i)
    return validMoves

def squareContains(x,y):
    ''' returns an object that contains the points x,y  '''
    for row in board:
        for square in row:
            if square.contains(x,y):
                return(square)

def containsPiece(pieces,square):
    for i in pieces:
        if square.containsShape(i):
            return(True)

def checkwin(pieces):
    # checks if the pieces are in the square win condition
    for row in range(4):
        for col in range(4):

            if containsPiece(pieces,board[row][col]) == True and containsPiece(pieces,board[row+1][col]) and containsPiece(pieces,board[row][col+1]) and containsPiece(pieces,board[row+1][col+1]):
                if pieces ==blueP:
                    return(True)
                else: 
                    return(False)
    # checks if they are four in a row
    for row in range(5):
        for col in range(2):

            if containsPiece(pieces,board[row][col]) == True and containsPiece(pieces,board[row][col+1]) and containsPiece(pieces,board[row][col+2]) and containsPiece(pieces,board[row][col+3]):
                if pieces ==blueP:
                    return(True)
                else: 
                    return(False)
    # checks if they are four in a row
    # checks for four column       
    for row in range(2):
        for col in range(5):

            if containsPiece(pieces,board[row][col]) == True and containsPiece(pieces,board[row+1][col]) and containsPiece(pieces,board[row+2][col]) and containsPiece(pieces,board[row+3][col]):
                if pieces ==blueP:
                    return(True)
                else: 
                    return(False)
    # check diagonally from bottom left to top right
    for row in range(3,5):
        for col in range(2):

            if containsPiece(pieces,board[row][col]) == True and containsPiece(pieces,board[row-1][col+1]) and containsPiece(pieces,board[row-2][col+2]) and containsPiece(pieces,board[row-3][col+3]):
                if pieces ==blueP:
                    return(True)
                else: 
                    return(False)
    # checks diagonals from top left to bottom right 
    for row in range(2):
        for col in range(2):

            if containsPiece(pieces,board[row][col]) == True and containsPiece(pieces,board[row+1][col+1]) and containsPiece(pieces,board[row+2][col+2]) and containsPiece(pieces,board[row+3][col+3]):
                if pieces ==blueP:
                    return(True)
                else: 
                    return(False)


def winScreen():
    # new window which pops up when called on which says who wins 
    win = tk.Tk()
    win.geometry("400x400")
    win.title("Win Screen")
    canvas = tk.Canvas(master = win, width = 400, height=400)
    canvas.pack()
    
    drawt = turtle.RawTurtle(canvas)
    if turncount%2==0:
        drawt.write('PLAYER 2 WINS', align='center', font=('Arial', 16, 'normal'))
    else:
        drawt.write('PLAYER 1 WINS', align='center', font=('Arial', 16, 'normal'))

    drawt.ht()

    win.mainloop()




def pauseScreen():
    # defines a function to run when button is clicked to open the instructions
    def Instructions():
        # reads file to use as label 
        labeltxt = open('teeko.txt','r')
        label = labeltxt.read()
        labeltxt.close()
        ins = tk.Toplevel(pause)
        ins.title('Instructions')
        ins.geometry("800x800")
        instruc = tk.Label(ins,text = label, pady = 100)
        instruc.pack()
        # opens image of the board to show user 
        boardimg2= tk.PhotoImage(file = 'boardimg.png')
        
        boardLabel = tk.Label(ins, image = boardimg2,pady = -200)
        boardLabel.image = boardimg2
        boardLabel.pack()
    # window which has 2 buttons, one to quut the menu and one to open instructions 
    pause = tk.Tk()
    pause.title('Pause Menu')
    pause.geometry("400x400")
    
    insButton = tk.Button(pause, text='Instructions', command = Instructions)
    insButton.place(x=175,y=100)
    
   

    quitButton = tk.Button(pause, text = 'Quit Menu', command = pause.destroy)
    quitButton.place(x=175,y =200)
    
    pause.mainloop()

def onMousePress(x,y):
    global turncount
    global moves 
    # if the user doesnt click on the board, the player is told to click on the board 
    if x not in range(100,301) or y not in range(100,301):
        playerLabel.value = 'CLICK ON THE BOARD'

    else:
        # player 1 turns
        if turncount % 2 == 0:
            
            # player 1's first 4 moves is in this if statemnt 
            if turncount <8:
                try:
                    square = squareContains(x,y)
                    
                    
                except:
                    pass
                
                if isemptySpace(square) is False:
                    
                    playerLabel.value = "PLAYER 1 PICK ANOTHER SQUARE"
                    square = squareContains(x, y)
                else:
                    blueP[int(turncount / 2) %4].centerX = square.centerX
                    blueP[int(turncount / 2) %4].centerY = square.centerY
                    checkersound.play()
                    playerLabel.value = 'PLAYER 2 TURN'
                    turncount+=1

                    return 
            # everymove after 8 turns if needed 
            else:
                for piece in blueP:
                    if piece.contains(x,y):
                        app.selected = piece
                        square = squareContains(x,y)
                        # START HERE TOMORROW
                        validMove = validMoves(square)
                        
                        if len(validMove) == 0:
                            app.selected = None
                            playerLabel.value = 'PLAYER 1 PICK ANOTHER SQUARE'
                            break
                        moves = validMove
                        
        # player 2 moves 
        if turncount % 2 == 1 :
            
            if turncount <8:
                square = squareContains(x,y)
                if isemptySpace(square) is False:
                    playerLabel.value = "PLAYER 2 PICK ANOTHER SQUARE"
                    square = squareContains(x,y)
                # player 2 moves after 8 moves 
                else:
                    redP[int(turncount / 2) % 4].centerX = square.centerX
                    redP[int(turncount / 2) % 4].centerY = square.centerY
                    checkersound.play()
                    playerLabel.value = 'PLAYER 1 TURN'
                    turncount+=1
            else:
                for piece in redP:
                    if piece.contains(x,y):
                        app.selected = piece
                        square = squareContains(x,y)
                        # START HERE TOMORROW
                        validMove = validMoves(square)
                        
                        if len(validMove) == 0:
                            app.selected = None
                            playerLabel.value = 'PLAYER 2 PICK ANOTHER SQUARE'
                            break
                        moves = validMove
            
            

def onMouseRelease(x,y):
    global turncount
    
    if app.selected != None:
        
        square = squareContains(x,y)
        if square in moves:
            app.selected.centerX = square.centerX
            app.selected.centerY = square.centerY
            checkersound.play()
            app.selected = None
            turncount+=1

            if turncount%2 ==0:
                
                playerLabel.value = 'PLAYER 1 TURN'
            else:
                
                playerLabel.value = 'PLAYER 2 TURN'
    if turncount%2 == 0 :
        if checkwin(redP) ==False:
            app.quit() 
            winScreen()
            
    else:
        if checkwin(blueP) ==True:
            app.quit()
            winScreen()
# if the key P is pressed, then the menu is opened 
def onKeyPress(key):
    if key =='p':
        print(1)
        app.paused = True
        pauseScreen()
        app.paused = False



pauseScreen()
board = drawWindow()
checkersound = Sound('https://cdn.freesound.org/previews/351/351518_4502687-lq.mp3')
playerLabel = Label('PLAYER 1 TURN',200,350)
blueP = [Circle( 50,180+i*20 ,10, fill = 'blue') for i in range(4)]
redP = [Circle( 350,180+i*20,10, fill = 'red') for i in range(4)]
app.selected = None
turncount = 0











cmu_graphics.run()