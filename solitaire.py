# Omiros Chatziiordanis AM 5388

def print_board():                                                             # function for printing the board
  for i in range(8):                                                           # repeat in the lines of the board
     for j in range(8):                                                        # repeat in the collumns (aka every object inside line i) of the board      ##both lines will be used again for the same reason
         if board[i][j]==None:
             print(" ", end=" ")                                               # end= is used so that every object inside the board is printed at the same line, when we put the next print without the end, the print changes line ## the program prints nothing at the spots with value None
         else:
             print(board[i][j], end=" ")
     print()

def check_moves():                                                             # function for checking if the player can make anymore moves
    for i in range(1,8):                                                       # see lines 4 and 5
     for j in range(1,8):
      if board[i][j]==1:                                                       # we start with each position on the board that equals to 1 as the player needs to move a peg that exists
        if j-2 in [0,1,2,3,4,5,6,7] and board[i][j-2]==0 and board[i][j-1]==1:        # we first check if the position that the player is putting the peg, which is the farthest, is inside the board so that we don't get an index error, then we check if the player can make a move according to the rules ## direction left
                return True                                                           # the function stops immidiatly when an available move is found
        elif j+2 in [0,1,2,3,4,5,6,7] and board[i][j+2]==0 and board[i][j+1]==1:      # direction right
                return True
        elif i-2 in [0,1,2,3,4,5,6,7] and board[i-2][j]==0 and board[i-1][j]==1:      # direction up
                return True
        elif i+2 in [0,1,2,3,4,5,6,7] and board[i+2][j]==0 and board[i+1][j]==1:      # direction down
                return True

def check_input():                                                             # function for checking the input
    peg=str(input("Enter peg position followed by move (L, R, U, or D):"))                     # input for the peg that the player wants to move and where
    if  len(peg)!=3 or peg[0].upper() not in ("ABCDEFG") or peg[1] not in ("1234567"):         # the program checks if the input doesn't have the right length and the correct form for its first two letters so that it will print the appropiate error message
        print("Something wrong with your input!")
    elif peg[2].upper() not in ("LRUD"):                                       # if the input is correct on its length and its first two letters, we check if it is wrong on its third letters so that the appropiate error message about the direction appears
       print("Direction is not L or R or U or D!")
    else:
      return peg                                                               # if everything is correct then the function returns the string of the input so that the game can continue


def move():                                                                    # function makes the actual move
    cor=["A","B","C","D","E","F","G"]                                          # a list which contains all the letters that help guide the player through the lines of the board
    x=cor.index(peg[0].upper())+1                                              # the letters are all placed in the list like at the board and the board has 8 lines but one reserved for the numbers of the collumns, so if we find the position of the letter that the player chose in the list and we add 1, we get the cordinates for the lines
    y=int(peg[1])                                                              # the numbers that guide us through the collumns are 1 to 7, the board has 8 collumns but one is reserved for the letters, so if we get the number of the player's input, we get the cordinates for the collumns
    dic={"L":{"a":0,"b":-1},"R":{"a":0,"b":1},"U":{"a":-1,"b":0},"D":{"a":1,"b":0}}           # this dictionary helps so that ,depending on the third letter of the input, we get the modifications that are needed for the coordinates of the changing pegs
    a,b=dic[peg[2].upper()]["a"],dic[peg[2].upper()]["b"]                                     # a represents the change in the lines and b in the collumns
    if check_peg(a,b,x,y):                                                                    # we go and check if the player has chose an available move, if it is available the if will be True so we can continue to making the move
        board[x][y]=0                                                          # the peg that the player choses to use, it will be empty after the move so it takes the value of 0       ## the specific objects of the board can be changed without using techniques like global()
        board[x+a][y+b]=0                                                      # the peg the player takes with his move and also will become empty
        board[x+2*a][y+2*b]=1             # the position that the player places his peg, it will have a peg after the move so it takes the value of 1 ## a and b make the cordinates of the peg next to the player's peg, so the position that the peg will be placed uses 2a and 2b as it will be two times farther than the player's peg
        print_board()                                                          # we print the board with the new changes

def check_peg(a,b,x,y):                                                        # function for checking if the player selected an available peg and move
    if board[x][y]==None:                                                      # lines 48 and 50 check if there isn't an available peg and print the appropiate error message depending on their position on the board
        print("Given peg position is out of board!")
    elif board[x][y]==0:
        print("Given peg position does not have a peg!")
    else:
        if (y+2*b) in [1,2,3,4,5,6,7] and (x+2*a) in [1,2,3,4,5,6,7]:         # if there is an available peg, we start to check the positions around it ## we check again for an index error
          if board[x+2*a][y+2*b]==None:                                       # the error messages explain what the if and elifs look exactly for
                print("Moving peg will fall out of bounds!")
          elif board[x+a][y+b]!=1:
                print("No peg at next position to jump over!")
          elif board[x+a][y+b]==1 and board[x+2*a][y+2*b]==1:
                print("Landing position is occupied!")
          else:
                return True                                                   # if everything is alright the function returns the value True so that the move can be made
        else:
                print("Moving peg will fall out of bounds!")

board=[[None,"1","2","3","4","5","6","7"],["A",None,None,1,1,1,None,None],["B",None,None,1,1,1,None,None],["C",1,1,1,1,1,1,1],["D",1,1,1,0,1,1,1],["E",1,1,1,1,1,1,1],["F",None,None,1,1,1,None,None],["G",None,None,1,1,1,None,None]] # the board of the game at the start, it's a 2D board with lines and collumns being made with 8 lists, with 8 objects each, inside one list
print_board()                                                                 # we print the board for the first time
while check_moves():                                                          # the main loop of the game that continues to be executed thanks to the function that checks if there are available moves
    peg=check_input()                                                         # we take the value that check_input() returns in a variable so that we need to type it only once
    if peg:                                                                   # if there is an actual string after all the checks, the game continues, if the variable peg has the value of None then the programs asks once again an input from the player until he gets it right
     move()                                                                   # we call this function so that the move is made, if the move cannot be made, the program asks again an input from the player

c=0                                                                           # lines 72 to 77 are needed so that the program tells the player how many pegs have remained AFTER there are no more moves! So it doen't need to be a function as it is needed only once
for i in range(1,8):                                                          # see lines 4 and 5
  for j in range(1,8):
   if board[i][j]==1:
    c+=1
print("No more moves. The number of remaining pegs is",c)