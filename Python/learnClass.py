class Person:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first + "." + last + "@email.com").lower()

    def fullname(self):
        return "{} {}".format(self.first, self.last).lower()


emp_1 = Person("Ghasnhyam", "mahato", 100000)
emp_2 = Person("Manisha", "Singh", 120000)
print(emp_2.fullname())
print(emp_2.email)
