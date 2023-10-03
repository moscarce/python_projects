name = 'Grace Chizaram Martins'
name1 = 'grace maduekwe'

class FullName():
    def get_fullname(self, name):
        lst = name.split(' ')
        fname = ''
        for index in range(len(lst) - 1):
            lst[index] = lst[index].capitalize()
            fname += lst[index][0] + ". "
        return fname + lst[len(lst) - 1].capitalize()

    def sum_alpha_numeric(self,alpha_num):
        total = 0;
        for index in range(len(alpha_num)):
            if alpha_num[index].isnumeric():
                if alpha_num[index-1] == '-':
                    total -= int(alpha_num[index])
                else:
                    total += int(alpha_num[index])
        return total





