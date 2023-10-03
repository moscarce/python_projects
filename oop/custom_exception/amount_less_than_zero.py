class AmountLessThanZero(Exception):
    def __init__(self):
        super().__init__("Amount cannot be less than zero")