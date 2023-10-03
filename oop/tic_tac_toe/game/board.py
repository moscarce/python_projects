class Board:
    def __init__(self):
        self.__cells = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def display(self):
        print(f'''
WELCOME TO MOSCARCE TIC-TAC-TOE GAME

{self.__cells[1]} | {self.__cells[2]} | {self.__cells[3]}
----------
{self.__cells[4]} | {self.__cells[5]} | {self.__cells[6]}
---------- 
{self.__cells[7]} | {self.__cells[8]} | {self.__cells[9]}  
        ''')

    def refresh_cells(self):
        for index in range(len(self.__cells)):
            self.__cells[index] = ' '

    def update_cells(self, cell_no, player):
        if self.__cells[cell_no] == ' ':
            self.__cells[cell_no] = player

    def check_winner(self, player):
        if self.__cells[1] == player and self.__cells[2] == player and self.__cells[3] == player:
            return True
        elif self.__cells[4] == player and self.__cells[5] == player and self.__cells[6] == player:
            return True
        elif self.__cells[7] == player and self.__cells[8] == player and self.__cells[9] == player:
            return True
        elif self.__cells[1] == player and self.__cells[4] == player and self.__cells[7] == player:
            return True
        elif self.__cells[2] == player and self.__cells[5] == player and self.__cells[8] == player:
            return True
        elif self.__cells[3] == player and self.__cells[6] == player and self.__cells[9] == player:
            return True
        elif self.__cells[1] == player and self.__cells[5] == player and self.__cells[9] == player:
            return True
        elif self.__cells[3] == player and self.__cells[5] == player and self.__cells[9] == player:
            return True
        return False
