import os    
import random
import copy    
board = [' ',[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]    
player = 1    
   
########win Flags##########    
Win = 1    
Draw = -1    
Running = 0   
Stop = 1    
###########################    
Game = Running    
Mark = 'X'    
   
#This Function Draws Game Board    
def DrawBoard():
    print("  _________________")
    print(" |     |     |     |")
    print(" |  %c  |  %c  |  %c  |" % (board[1][1], board[1][2], board[1][3]))    
    print(" |_____|_____|_____|")
    print(" |     |     |     |")
    print(" |  %c  |  %c  |  %c  |" % (board[2][1], board[2][2], board[2][3]))    
    print(" |_____|_____|_____|")  
    print(" |     |     |     |")
    print(" |  %c  |  %c  |  %c  |" % (board[3][1], board[3][2], board[3][3]))    
    print(" |_____|_____|_____|")    
   
#This Function Checks position is empty or not    
def CheckPosition(x,y):    
    if(board[x][y] == ' '):    
        return True    
    else:    
        return False    

#This Function Checks game has drawn or not    
def CheckDraw():
    if ' ' not in board:
        return True
    return False
   
#This Function Checks player has won or not    
def CheckWin(p1,p2):    
    global Game  
    global player
    i=1
    while(i<4):
        #Horizontal winning condition    
        if(board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] != ' '):    
            player-=1    
            if(player%2!=0):    
                print(p1, " Won")
                Game=Win
                return 1
            else:    
                print(p2, " Won")
                Game=Win
                return 2   
        #Vertical Winning Condition    
        elif(board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] != ' '):    
            player-=1    
            if(player%2!=0):    
                print(p1, " Won")
                Game=Win  
                return 1
            else:    
                print(p2, " Won")
                Game=Win
                return 2
        i+=1

    #Diagonal Winning Condition    
    if(board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[1][1] != ' '):    
        player-=1    
        if(player%2!=0):    
            print(p1, " Won")
            Game=Win  
            return 1
        else:    
            print(p2, " Won")
            Game=Win
            return 2    
    elif(board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[1][3] != ' '):    
        player-=1    
        if(player%2!=0):    
            print(p1, " Won")
            Game=Win  
            return 1
        else:    
            print(p2, " Won")
            Game=Win
            return 2    
    #Match Draw Condition    
    elif(CheckDraw()):
        Game=Draw
        return 0
    #Keep Match Running
    else:            
        Game=Running
        return 3


def ai_game_play(name):
    global Game
    global player
    print(name,"='X', AI='O'")
    turn = random.randint(0,9) 
    if turn%2==0:
        p1=name
        p2="AI"
    else:
        p2=name
        p1="AI"
    player=1
    gamestate=3
    while(player<10 and gamestate!=1 and gamestate!=2): 
        if(turn % 2 == 0):  
            flag=1  
            print(name,"'s chance")
            while(flag==1):
                x = int(input("Enter the row between [1-3] where you want to mark: "))
                y = int(input("Enter the column between [1-3] where you want to mark: "))
                if x<=3 or x>=1 or y<=3 or y>=1:
                    print("Entry out of index!")
                    flag=0
                else:
                    flag=1
            Mark = 'X'    
        else:
            s=AI_move(name)
            x=s[0]
            y=s[1] 
            Mark = 'O'  
            if(CheckPosition(x,y)):
                print("AI's chance")
                print(s)
        if(CheckPosition(x,y)):
            board[x][y] = Mark  
            os.system('cls')
            DrawBoard() 
            turn+=1  
            player+=1
            gamestate=CheckWin(p1,p2)  
        else:
            if Mark == 'X':
                print("This tile is already filled!")
    if(gamestate==1 or gamestate==2):
            Game=Win
            if p1==name:
                if gamestate==1:
                    winadjust(name)
                elif gamestate==2:
                    loseadjust(name)
            elif p2==name:
                if gamestate==2:
                    winadjust(name)
                elif gamestate==1:
                    loseadjust(name)
                    
                
    elif(player==10):
        print("Game Draw")
        drawadjust(name)
        Game=Draw

def winadjust(name):
    for i in range(len(rating)):
        if rating[i][0]==name:
            rating[i][1]=int(((((rating[i][2]-1)*rating[i][1])+1200)/(rating[i][2])))
            print("rating =",rating[i][1])


def loseadjust(name):
    for i in range(len(rating)):
        if rating[i][0]==name:
            rating[i][1]=int(((((rating[i][2]-1)*rating[i][1])+800)/(rating[i][2])))
            print("rating =",rating[i][1])
    
def drawadjust(name):
    for i in range(len(rating)):
        if rating[i][0]==name:
            rating[i][1]=int(((((rating[i][2]-1)*rating[i][1])+1000)/(rating[i][2])))
            print("rating =",rating[i][1])
    
def testwin(b,k):
    return ((b[1][1]==k and b[1][2]==k and b[1][3]==k) 
            or
            (b[2][1]==k and b[2][2]==k and b[2][3]==k) 
            or
            (b[3][1]==k and b[3][2]==k and b[3][3]==k) 
            or
            (b[1][1]==k and b[2][1]==k and b[3][1]==k) 
            or
            (b[1][2]==k and b[2][2]==k and b[3][2]==k) 
            or
            (b[1][3]==k and b[2][3]==k and b[3][3]==k) 
            or
            (b[1][1]==k and b[2][2]==k and b[3][3]==k) 
            or
            (b[1][3]==k and b[2][2]==k and b[3][1]==k))

def test_win_move(b, sign, m, n):

    bcopy = copy.deepcopy(b)
    bcopy[m][n] = sign
    return testwin(bcopy, sign)

def trycastle(b, sign, m, n):
    bcopy = copy.deepcopy(b)
    bcopy[m][n] = sign
    strat=0
    for g in range(0,9):
        if test_win_move(bcopy, sign, int(g/3)+1, (g%3)+1) and bcopy[int(g/3)+1][(g%3)+1]== ' ':
            strat+=1
    return(strat>=2)

def mediummove(b):

    for i in range(0, 9):
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ' and test_win_move(board, 'O', m, n):
            return i
    
    for i in range(0, 9):
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ' and test_win_move(board, 'X', m, n):
            return i

    for i in [0, 2, 6, 8]:
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ':
            return i

    if board[2][2]== ' ':
        return 4

    for i in [1, 3, 5, 7]:
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ':
            return i 



def hardmove(b,name):

    for i in range(0, 9):
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ' and test_win_move(board, 'O', m, n):
            return i
    
    for i in range(0, 9):
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ' and test_win_move(board, 'X', m, n):
            for j in range(len(rating)):
                if rating[j][0]==name:
                    rating[j][1]+=3
            return i
        

    for i in range(0,9):
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ' and trycastle(board, 'O', m, n):
            return i
    usercastles=0
    for i in range(0,9):
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ' and trycastle(board, 'X', m, n):
            usercastles+=1
            fake=i
    if usercastles==1:
        for j in range(len(rating)):
            if rating[j][0]==name:
                rating[j][1]+=10
        return fake
    elif usercastles==2:
        for i in range(len(rating)):
            if rating[i][0]==name:
                rating[i][1]+=20
        for j in [1, 3, 5, 7]:
            o=int(j/3)+1
            p=(j%3)+1
            if board[o][p] == ' ':
                return j 

    if board[2][2]== ' ':
        return 4
    
    #cornerside=[0,1,2,3,5,6,7,8]
    #while(1):
        ranmove=random.randint(0,7)
        #print('in while loop')
        m=int(cornerside[ranmove]/3)+1
        n=(cornerside[ranmove]%3)+1
        if(CheckPosition(m,n)):
            return cornerside[ranmove]
    for i in [0, 2, 6, 8]:
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ':
            return i
        
    for i in [1, 3, 5, 7]:
        m=int(i/3)+1
        n=(i%3)+1
        if board[m][n] == ' ':
            return i


def AI_move(name):
    while(1):
        if diff==1:
            move=random.randint(0,8)
            i=int(move/3)+1
            j=(move%3)+1
            s=[i,j]
            return s
        elif diff==2:
            move=mediummove(board)
            i=int(move/3)+1
            j=(move%3)+1
            s=[i,j]
            return s
        elif diff==3:
            move=hardmove(board,name)
            i=int(move/3)+1
            j=(move%3)+1
            s=[i,j]
            return s
        else:
            print("Not a valid difficulty!")


def game_play(player1,player2):
    global Game
    global player
    turn = random.randint(0,9) 
    if turn%2==0:
        p1=player1
        p2=player2
    else:
        p2=player1
        p1=player2
    player=1
    gamestate=3
    while(player<10 and gamestate!=1 and gamestate!=2):
        flag=1 
        if(turn % 2 == 0):    
            print(player1,"'s chance")

            while(flag==1):
                x = int(input("Enter the row between [1-3] where you want to mark: "))
                y = int(input("Enter the column between [1-3] where you want to mark: "))
                if x<=3 or x>=1 or y<=3 or y>=1:
                    print("Entry out of index!")
                    flag=0
                else:
                    flag=1
            Mark = 'X'    
        else:
            print(player2,"'s chance")
            while(flag==1):
                x = int(input("Enter the row between [1-3] where you want to mark: "))
                y = int(input("Enter the column between [1-3] where you want to mark: "))
                if x<=3 or x>=1 or y<=3 or y>=1:
                    print("Entry out of index!")
                    flag=0
                else:
                    flag=1
            Mark = 'O'  
            
        if(CheckPosition(x,y)):
            board[x][y] = Mark  
            os.system('cls')
            DrawBoard() 
            turn+=1  
            player+=1
            gamestate=CheckWin(p1,p2)  
        else:
            print("This tile is already filled!")
    if(player==10):    
        print("Game Draw")
        Game=Draw
    elif(gamestate==1 or gamestate==2):
            Game=Win

def vsai(name):   
    os.system('cls')    
    DrawBoard() 
    ai_game_play(name)   

def pvp():
    os.system('cls')
    DrawBoard()
    player1=input("Name of player 1:\n")
    player2=input("Name of player 2:\n")
    game_play(player1, player2)

def resetboard():
    global board
    board = [' ',[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
os.system('cls')
print("Tic-Tac-Toe Game")    
print()    
print()    
print("Please Wait...")    
print()
flag=0
rating=[]
while(flag==0):
    resetboard()
    mode=int(input("Game Mode:\n1. vs AI\n2. PvP\nEnter the number:\n"))
    if mode!=1 and mode!=2:
        print()
        print("Not a valid game mode!")
        print()
        print()
    elif mode==1:
        name=input("Enter your name:\n")
        slog=0
        if len(rating)==0:
            print()
            print("Welcome",name,"!")
            rating.append([name,1000,0])
            slog=1
        else:
            for i in range(len(rating)):
                if rating[i][0]!=name:
                    print()
                    print("Welcome",name,"!")
                    rating.append([name,1000,0])
                    slog=1
        if slog==0:
            print("Welcome back",name,"!")

        
        num=int(input("\nHow many matches do you want to play against AI? \n(Play at least one match in Hard Mode to find your rating)\n"))
        for i in range(0,num):
            resetboard()
            diff=int(input("Enter the difficulty level from the following options:\n1. EASY \n2. MEDIUM \n3. HARD \n"))
            if diff==3:
                for i in range(len(rating)):
                    if rating[i][0]==name:
                        rating[i][2]+=1
            vsai(name)
            for i in range(len(rating)):
                    if rating[i][0]==name and rating[i][2]>=3:
                        print("Your rating is: ", rating[i][1])
                        
            print()
            print("-----------------")

    elif mode==2:
        pvp()
    print()
    print("-----------------")