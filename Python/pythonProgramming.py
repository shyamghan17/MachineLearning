fruit = "Banana"
# print(fruit)
#
# print(fruit[0], ",", fruit[5])
#
# length = len(fruit)
# print(length)
#
# for i in fruit:
#     print(i)


# riverse the string
#
# startingIndex = len(fruit) - 1
# stopindex = -1
# step = -1
#
# for i in range(len(fruit)-1, -1, -1):
#     print(fruit[i])
#
# print(' ')
#
# startindex = 0
# endindex = len(fruit)
# steps = 1
#
# for i in range(startindex, endindex, steps):
#     print(fruit[i])
#
#     number = range(0, 200, 5)
#
#     for i in number:
#         print(i)
# #
# s = 'popular Python'
#
# print(s[0:7],'is', s[8:])
# is string mutable
greeting = "welcome to party"
#
# length = len(greeting)
# print(length)
#
# greeting[0] = 'v'
# print(greeting)

# new_greeting = 'V' + greeting
# print(new_greeting)
#
# word = 'banana'
# count = 0
# startindex = 0
# stopindex = len(word)
# step = 1
#
# for i in range(startindex, stopindex, step):
#     print(i, ' ', word[i])
#     if(word[i] == 'a'):
#         count = count+1
#
# print('count word "b"', count)
#
# print('...........................')
# word = input('please provide a word for a string comparison ')
# word = word.lower()
# if(word<'banana'):
#     print('your word is ', word, 'comes before banana.')
# elif word > 'banana':
#     print('your word is ', word, 'comes before banana.')
# else:
#     print('all right banana.')
# c = [10, 20, 30, 40, 50, 10, 50, 60]
# d = ["zebra", "ram", "lark"]
# print(c, type(c))
# print(d, type(d))
#
# print(min(c), max(c))
# print(c.count(10))

# word = "apple"
# count = []
# startindex = 0
# endendex = len(word)
# step = 1
# for i in range(startindex, endendex, step):
#     if word[i] == "p":
#         count.append(word[i])
# print(count, "count")
# #
# t= ['A', 'B', 'C']
# print(t)
# t.append('D')
# length = len(t)
# for i in range(0, length):
#     print(t[i].lower())
#
# name = 'ghanshyam kumar mahato'
# string = []
# for i in range(0, len(name)):
#     print(name[i])
#     if len(string) == 0:
#         string.append(name[i])
#     else:
#         for j in range(0, len(string)):
#             if name[i] != string[j]:
#                 string.append(name[i])
#             pass
#
# print(string)

numbers = [10, 20, 30, 40]
sum = 0
length = len(numbers)
for i in range(0, length):
    sum= sum+numbers[i]
print('sum of all numbers is: ', sum)
print('average of all numbers is: ', sum/length)


class Employee:




    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@kushawaha.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    emp_1 = Employee('ram', 'shyam', 100000)
    emp_2 = Employee('manisha', 'singh', 120000)
