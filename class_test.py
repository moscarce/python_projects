class Test:
    def __init__(self,fname : str,lname : str):
        self.fname = fname
        self.lname = lname
    def draw(self):
        print('hello')

    def __str__(self):
        return f'{self.fname} {self.lname}'


test = Test('Akinjokun','Oluwatobi')
print(test)