class SecondLargest():
    def __init__(self):
        self.__second_max = 0

    def check_second_largest(self,question):
        max = -1
        for character in question:
            if character.isdigit():
                num = int(character)
                if num > max:
                    self.__second_max = max
                    max = num

        return self.__second_max




