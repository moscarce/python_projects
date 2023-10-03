from menstrual_class import MenstrualCycleTracker
from menstrual_class import SeeADoctor


class MenstrualApp:

    @staticmethod
    def __collect_cycle_length():
        length = input('''Enter your cycle length
NOTE: The menstrual cycle length is the number of days from the first day of one menstrual period (cycle start)
to the day before the next menstrual period begins (cycle end).
>>>>>>  
''')
        length = length.strip()
        while not length.isdigit():
            print('please enter a valid length')
            length = input('''Enter your cycle length
NOTE: The menstrual cycle length is the number of days from the first day of one menstrual period (cycle start)
to the day before the next menstrual period begins (cycle end).
>>>>>>  ''')

        return int(length)

    @staticmethod
    def __proceed(tracker):
        print(f'''
    CYCLE LENGTH = {tracker.get_cycle_length()} DAYS
    OVULATION DAY = DAY {tracker.get_ovulation_day()}
    POSSIBLE OVULATION DAYS = {tracker.get_possible_ovulation_days()}
    FULL LENGTH OF OVULATION DAYS = {tracker.get_ovulation_days_full_length()}

    OVULATION DAY -> This is scientifically proven

    POSSIBLE OVULATION DAYS ->  ovulation can occur approximately 2 days before or 2 days after the expected day.
    It accounts for the natural variation in the timing of ovulation in different menstrual cycles.

    FULL LENGTH OF OVULATION DAYS -> Sperm can survive in the female reproductive tract for up to five days.
    So, the fertile window extends a few days before ovulation.

    SAFE PERIOD -> Any other day that is not between {tracker.get_ovulation_days_full_length()}
            ''')

    @staticmethod
    def start():
        tracker = MenstrualCycleTracker()
        cycle_length = MenstrualApp.__collect_cycle_length()
        try:
            tracker.set_cycle_length(cycle_length)
            MenstrualApp.__proceed(tracker)
        except SeeADoctor:
            print('''
The common cycle length is between 21 to 35 days
Please see a doctor as your cycle length is rare one
            ''')
