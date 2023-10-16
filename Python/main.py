# from util import *
# n = 3
# m = 4
# result1 = to_square(n)
# result2 = to_square(m)
#
# print(result1)
# print(result2)

# def get_grade(score):
#     if score >=90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     return grade
# def get_phone_bill(gb):
#     if gb <= 15:
#         bill = 100
#     elif gb > 15:
#         bill = 100 + (gb-15)*1000 * 0.10
#     return bill
#
#
# print(get_phone_bill(16))
# #%%

#
# num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
# def percentage_growth(num_users, yrs_ago=1):
#     growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
#     print(num_users[len(num_users)-yrs_ago], 'this')
#     return growth
#
# # Do not change: Variable for calculating some test examples
# num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
#
# # # Do not change: Should return .036
# print(percentage_growth(num_users, 1))
# #
# # # Do not change: Should return 0.66
# print(percentage_growth(num_users_test, 7))

# spam_amount = 0
#
#
# # Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
# spam_amount = spam_amount+1
#
# if spam_amount > 0:
#     viking_song = "But I don't want ANY spam!"
# else:
#     viking_song = "Spam" * spam_amount
# print(viking_song
x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
# print(c.imag)