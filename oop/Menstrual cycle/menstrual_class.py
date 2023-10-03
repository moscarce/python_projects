class SeeADoctor(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MenstrualCycleTracker:
    def __init__(self):
        self.__cycle_length = None
        self.__ovulation_day = None
        self.__possible_ovulation_days = None
        self.__ovulation_days_full_length = None

    def set_cycle_length(self, cycle_length):
        if 20 < cycle_length < 36:
            self.__cycle_length = cycle_length
            self.__ovulation_day = cycle_length - 14
            self.__possible_ovulation_days = f'DAY {self.__ovulation_day - 2} - DAY {self.__ovulation_day + 2}'
            self.__ovulation_days_full_length = f'DAY {self.__ovulation_day - 7} - DAY {self.__ovulation_day + 2}'
        else:
            raise SeeADoctor()

    def get_cycle_length(self):
        return self.__cycle_length

    def get_ovulation_day(self):
        return self.__ovulation_day

    def get_possible_ovulation_days(self):
        return self.__possible_ovulation_days

    def get_ovulation_days_full_length(self):
        return self.__ovulation_days_full_length
