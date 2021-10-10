def print_board_numeration():
    print("This is the numeration of the board:")
    print("|  1  |  2  |  3  |")
    print("|  4  |  5  |  6  |")
    print("|  7  |  8  |  9  |")


def player_write_names():
    bot_1, bot_2 = input("Player one name: "), input("Player two name: ")
    possible_signs = ["X", "O"]
    bot_1_sign = input(f"{bot_1}, would you like to play with 'X' or 'O'? ")
    possible_signs.remove(bot_1_sign)
    bot_2_sign = possible_signs[0]
    return [bot_1, bot_1_sign], [bot_2, bot_2_sign]


def print_board(matrix):
    for el in matrix:
        print(el)


def apply_player_choice():
    pass


def player_choice():
    pass


def play(matrix, bot_1, bot_2):
    print_board_numeration()
    while True:
        break


def generate_board(size):
    return [[None]*size for x in range(size)]


board = generate_board(3)
player1, player2 = player_write_names()
print_board_numeration()

