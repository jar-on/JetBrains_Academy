winners = set()  # set used to avoid duplicate winners and quickly find impossible situations (2 winners)
game_state = [[" " for i in range(3)] for j in range(3)]  # generates a 3x3 matrix of ' '
playing = True
player = "X"


def show_board(state):
    '''Displays the play board'''
    print("---------")
    for line in state:
        print("|", " ".join(line), "|")
    print("---------")


def who_won(game_state):
    global playing
    '''Checks for possible winners and impossible situations'''
    # check for win in lines
    for line in game_state:
        if all(element == "X" for element in line):
            winners.add("X")
        if all(element == "O" for element in line):
            winners.add("O")

    # check for win in columns
    for column in range(3):
        if all(row[column] == "X" for row in game_state):
            winners.add("X")
        if all(row[column] == "O" for row in game_state):
            winners.add("O")

    # check for win in diagonals    
    if game_state[0][0] == game_state[1][1] == game_state[2][2]:
        winners.add(game_state[1][1])
    if game_state[0][2] == game_state[1][1] == game_state[2][0]:
        winners.add(game_state[1][1])

    if "X" in winners:
        print("X wins")
        playing = False
    elif "O" in winners:
        print("O wins")
        playing = False
    # check for any _ that indicate that the game still continues
    elif not any(" " in line for line in game_state):
        print("Draw")
        playing = False


def get_move(game_state):
    global player
    checking = True
    while checking:
        data = input("Enter the coordinates:").split()
        if not data[0].isnumeric() or not data[1].isnumeric():
            print("You should enter numbers!")
            continue
        elif int(data[0]) not in (1, 2, 3) or int(data[1]) not in (1, 2, 3):
            print("Coordinates should be from 1 to 3!")
            continue
        elif game_state[int(data[0]) - 1][int(data[1]) - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            game_state[int(data[0]) - 1][int(data[1]) - 1] = player
            player = "O" if player == "X" else "X"
            checking = False
            return game_state


show_board(game_state)
while playing:
    get_move(game_state)
    show_board(game_state)
    who_won(game_state)
