def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-"*9)
    print()
def chek_win(board,player):
    for row in board:
        if all(cell == player for cell in row):
           return True
        for col in range(3):
           if all(board[row][col] == player for row in range(3)):
                  return True
           if all(board[i][i] == player for i in range(3)):
                  return True
           if all(board[i][2-i]==player for i in range(3)):
                  return True
    return False
def check_draw(board):
    return all(cell != " " for row in board for cell in row)
def play_game():
    board =[[" " for _ in range(3)] for _ in range(3)]
    current_player = "x"
    while True:
       print_board(board)
       print(f"player {current_player}'s turn.")
       try:
                  row=int(input("Enter row (0,1,2): "))
                  col=int(input("Enter column (0,1,2): "))
       except ValueError:
                  print("Invalid input please enter number only")
                  continue
       if row not in range(3) or col not in range(3):
                  print("invlaid position try again.")
                  continue
       board[row][col] =current_player
       if check_win(board , current_player):
                  print_board(board)
                  print(f"Player {current_player} wins!")
                  break
       current_player="o" if current_player == "x" else "x"
       if _name_ =="_main_":
                  play_game()
                  
                  
