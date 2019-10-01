import itertools as it
from colorama import Fore, Back, Style,init
init()
def place(game_board,row=0,column=0,player=0,just_display=False):
    try:
        if not just_display:
            if game_board[row][column]!=0:
                print("Already occupido position")
                #return True
            else:    
                game_board[row][column]=player
        game_size=len(game_board)
        print("   "+"  ".join(str(i) for i in range(game_size))) 
        for index,row in enumerate(game_board):
            colored_row=""
            for items in row:
                if items==0:
                    colored_row+="   "
                elif items==1:
                    colored_row+=Fore.GREEN + " X "+Style.RESET_ALL
                elif items==2:
                    colored_row+=Fore.MAGENTA + " O "+Style.RESET_ALL 
            print(index,colored_row)    
        return game_board  
        #return True
    except IndexError as error:  
        print("Dumb head you entered ",error," Chance gone")
        return game_board
        #return True
    except Exception as e:
        print("Something went wrong",e)
        return game_board
        #return True
  
def win(game_board):
    
    def check(l):
        if l.count(l[0])==len(row) and l[0]!=0:
            return True
        return False
    def check_zero(game_board):
        for row in game_board:
        	for item in row:
        		if item ==0:
        		 return True
        return False		

   
    #Horizontally
    for row in game_board:
        if check(row):
         print(f"Player {row[0]} won horizontally-")
         return True,True
    #vertically
    for c in range(len(game_board)):
        col=[]
        for row in game_board:
            col.append(row[c])
        if check(col):
         print(f"Player {col[0]} won vertically|")  
         return True,True
    #diagonally
    dia=[]
    for i in range(len(game_board)):
      dia.append(game_board[i][i])
    if check(dia):
     print(f"Player {dia[0]} won diagonally \\")  
     return True,True
    
    dia=[]
    for i,j in zip(range(len(game_board)),reversed(range(len(game_board)))):
        dia.append(game_board[i][j])
    if check(dia):
     print(f"Player {dia[0]} won diagonally /")      
     return True,True
    if check_zero(game_board):
     return False,False 
    return False,True

play=True

while play:
    board_size=int(input("Enter the size of board: "))
    game_board=[[0 for j in range(board_size)]for i in range(board_size)]
    place(game_board,just_display=True)
    curr_game=False
    end=False
    player_choice=it.cycle([1,2])
    while not curr_game and not end:
        current_player=next(player_choice)
        print(f"Current Player: {current_player}")
        row=int(input("Enter the row to enter: "))
        col=int(input("Enter the column to enter: "))
        game_board=place(game_board,row,col,current_player)
        curr_game,end=win(game_board)
    if end:
       i=input("Game Ended.Wanna Continue ? (Y/N) ")
       if i.lower()=='y':
         print("Loading . .")
       else :
         print("Bye")
         play=False    
