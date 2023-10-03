class InsufficientFund(Exception):
    def __init__(self):
        super().__init__("Insufficient fund")