from random import randrange


class PencilGame:

    def __init__(self):
        self.player_1 = "Player"
        self.player_2 = "Bot"
        self.pencil_no = self.get_pencil_no()
        self.is_bot_turn = self.get_first_player()

    def play(self):
        """Main game loop"""
        while self.pencil_no > 0:
            print('|' * self.pencil_no)
            print(f"{self.get_current_player()}'s turn:")
            self.pencil_no -= self.get_removed_pencils()
            self.is_bot_turn = not self.is_bot_turn
            if not self.pencil_no:
                print(f'{self.get_current_player()} won!')

    def get_current_player(self):
        if self.is_bot_turn:
            return self.player_2
        return self.player_1

    def get_pencil_no(self):
        """Sets the number of pencils for the beginning of the game"""
        print('How many pencils would you like to use:')
        while True:
            try:
                pencil_no = int(input())
            except ValueError:
                print("The number of pencils should be numeric")
                continue
            if pencil_no <= 0:
                print('The number of pencils should be positive')
                continue
            return pencil_no

    def get_first_player(self):
        """Sets the selected_player for the beginning of the game"""
        print(f'Who will be the first({self.player_1}, {self.player_2}):')
        while True:
            selected_player = input()
            if selected_player not in (self.player_1, self.player_2):
                print(f'Choose between {self.player_1} and {self.player_2}')
                continue
            if selected_player == self.player_2:
                return True
            return False

    def get_removed_pencils(self):
        """Gets a valid number of pencils to remove"""
        # algorithm to use during bot's turn
        if self.is_bot_turn:
            if self.pencil_no == 1:
                print(1)
                return 1
            move_evaluation = self.pencil_no % 4
            if move_evaluation == 0:
                print(3)
                return 3
            if move_evaluation == 1:
                random_move = randrange(1, 4)
                print(random_move)
                return random_move
            print(move_evaluation - 1)
            return move_evaluation - 1

        # loop for the player's turn
        while True:
            try:
                removed_pencils = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
                continue
            if removed_pencils not in (1, 2, 3):
                print("Possible values: '1', '2' or '3'")
                continue
            if removed_pencils > self.pencil_no:
                print('Too many pencils were taken')
                continue
            return removed_pencils


game = PencilGame()
game.play()
