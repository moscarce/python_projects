from pythonProject.oop.tic_tac_toe.game.board import Board


class Game:
    __lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    __board = Board()

    @staticmethod
    def __restart():
        choice = input('Do you want to play again? [Y / N] : ')
        choice = choice.strip().lower()
        match choice:
            case 'y':
                Game.__board.refresh_cells()
                Game.__lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                Game.start()
            case 'n':
                exit(69)
            case _:
                print('Invalid input')
                Game.__restart()

    @staticmethod
    def __collect_position(player):
        player = player.capitalize().strip()
        position = input(f'{player}) Turn >>>[1-9]: ')
        position = position.strip()
        while not position.isdigit() or position not in Game.__lst:
            print('Invalid move')
            position = input(f'{player}) Turn >>>[1-9]: ')
        position = int(position)
        Game.__lst.remove(str(position))
        return position

    @staticmethod
    def __collect_choice(player):
        choice = input(f'{player} Choose a character to to play as: ')
        choice = choice.strip()
        while len(choice) != 1 or choice == ' ':
            print('Invalid input')
            choice = input(f'{player} Choose a character to to play as: ')
        return choice

    @staticmethod
    def __play(player_choice):
        Game.__board.display()
        player_move = Game.__collect_position(player_choice)
        Game.__board.update_cells(player_move, player_choice)
        if Game.__board.check_winner(player_choice):
            Game.__board.display()
            print(f'{player_choice} WINS!!!')
            Game.__restart()
        elif len(Game.__lst) == 0:
            Game.__board.display()
            print("IT'S A TIE!!!")
            Game.__restart()

    @staticmethod
    def start():
        p1_choice = Game.__collect_choice('Player 1,')
        p2_choice = Game.__collect_choice('Player 2,')
        p1_choice = p1_choice.strip().capitalize()
        p2_choice = p2_choice.strip().capitalize()
        while True:
            Game.__play(p1_choice)
            Game.__play(p2_choice)

