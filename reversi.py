# simple board game "reversi"
print("Hello and Wellcome to board game Reversi")
print("please choose the size of the board: (between: 4-16) ")
board = {}


def table_printer(size):
    for j in range(1, size + 1):
        for i in range(1, size + 1):
            if(j == 1 and i == 1):
                for index in range(1, size + 1):
                  # for n in make_arr():
                   # board[1][index] = index
                    # print(board)
                    print("   ", index,  end="")
                print()

            if(i == 1):

                print("  ", " --- "*size)
                #print(j, end=" ")

                print(j,  "|   |"*(int(size*1.1)),  end=" ")
        print("")
    print("  ", " --- "*size)
    print("lets play reversi:")


def make_arr(size):
    arr = [[" | " for x in range(size)] for y in range(size)]
    return arr


size = int(input())
if size % 2 != 0:
    print("Please choose an even number:")
    size = int(input())

player_one = " | O |"
player_two = " | x |"

board = make_arr(size)
# coordinate for the player
x_coord = int(size / 2)  # horezontal, row number
y_coord = int(size / 2)  # vertical; column number
# stsr vaslue for palyer one and two
board[x_coord][y_coord] = player_one
board[x_coord-1][y_coord-1] = player_one
board[x_coord-1][y_coord] = player_two
board[x_coord][y_coord-1] = player_two

table_printer(size)
