import random
board = [[1,2,3],[4,5,6],[7,8,9]]

def DisplayBoard(board):
    for row in board:
        count = 1
        for i in row:
            print("       "+ str(i), end="")
            if count % 3 == 0:
                  print("\n")
                  
            count += 1
   

DisplayBoard(board)


def MakeListOfFreeFields(board):
    free_sq =[]
    for row in board:
        for i in row:
            if type(i) == int:
                #The block is empty
                _row = row.index(i)
                _col = board.index(row)
                free_sq.append((_row, _col))
    print("Free squares:", free_sq)


def VictoryFor(board, sign):
    num = 0
    for i in range(len(board)):
        if (board[0][num] == board[1][num] == board[2][num] == sign):
            print(sign, "Has won the game Vertically")
            return True
        num += 1
            

    for row in board:
        if (row.count(sign) == len(row)):
            print(sign, "Has won the game Horizontally")
            return True

   
    if (board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign):
        print(sign, "Has won the game Diagonally")
        return True
    else:
        return False
            

def DrawMove(board):
    empty_spot = []
    for row in board:
        for i in row:
            if type(i) == int:
                empty_spot.append(i)

    random_spot = random.choice(empty_spot)
    for row in board:
        for i in row:
            if (random_spot == i):
                row[row.index(random_spot)] = "X"

    
def EnterMove(board):
    move = int(input("Enter move 1-9: "))
    
    for row in board:
        #line
        if move in row:
                #Shows that spot has not been played yet
                row[row.index(move)] = "O"
                break
        else:
            played_spot = True
    

has_won = False
while not has_won:
    MakeListOfFreeFields(board)
    EnterMove(board)
    if (VictoryFor(board, "O")):
        break
    DrawMove(board)
    if (VictoryFor(board, "X")):
        break

    DisplayBoard(board)

    
