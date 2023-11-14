class Employee:
    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + 'last' + '@kushawaha.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('ghanshyam', 'mahato', 100000)
emp_2 = Employee('manha', 'singh', 120000)

print(emp_1.fullName())