class IncorrectPin(Exception):
    def __init__(self):
        super().__init__("Pin is incorrect")