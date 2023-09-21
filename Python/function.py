def hello_function(greeting, name='you'):
    return '{}, {}'.format(greeting, name)

print(hello_function(name='hi', greeting='ghanshyam'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses = ('math', 'arts')
info = {'name': 'ghanshyam', 'age': 22}

student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31]
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1<= month<= 12:
        return 'Invalid Month'
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month]

print(days_in_month(2010, 2))