'''functions'''

# def varma(self):
#     print("this is function",self)
# varma(100)

# def varma(aa):
#     print("this is function",aa)
# varma(100)

# def varma(a,b,c):
#     print("this is function",a,b,c)
# varma(100,33,34)

# def varma(a,b):
#     print(a+b)
# varma(100,33)
# varma(10,33)

# def varma(name):
#     print("hii",name)
# n = input("Enter the name:")
# varma(n)

# def sunny(*name):        #arbitary parameters
#     print("hii",name)
# sunny(1,23,19,26,18)

# def sunny(**name):
#     print("hii",name)
# sunny(name="ram",age=25)

# def outerfunction():
#     print("this is outer function")
#     def innerfunction():
#         print("this is inner function")
#     innerfunction()
# outerfunction()

# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)

# '''Advance Functions'''

# """lambda function """
# f = lambda a:a*a  #syntax

# x = lambda a,b,c:a+b+c
# a = int(input())
# b = int(input())
# c = int(input())
# print(x(a,b,c))

# l1=[12,34,5,6,8]
# l2=[]
# for i in l1:
#     t = lambda a:a+1
#     l2.append(t(i))
# print(l2)

# """Filter function"""

# #syntax:-filter(function,sequence)

# ages = [5,12,17,18,24,32]
# def myfunc(x):
#     if x<18:
#         return False
#     else:
#         return True
# adults = filter(myfunc,ages)
# print(list(adults))

# """Map function"""

# def calculateaddition(n):
#     return n+n
# numbers=(1,2,3,4)
# result=map(calculateaddition,numbers)
# print(list(result))

# """Reduce function"""

# from functools import reduce
# d = reduce(lambda a,b:a+b,[23,21,45,98])
# print(d)

# from functools import reduce
# num = [23,21,45,98]
# varma = lambda a,b:a+b
# d = reduce(varma,num)
# print(d)

# """Generator function"""

# def simpleGeneratorfun():
#     yield 1
#     yield 2
#     yield 3
# x = simpleGeneratorfun()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# #diff bwt filter AND map

# # def even(x):
# #     if x%2==0:
# #         print(x)
# nums = [11,22,33,44,55]
# map = list(map(lambda x:x**2,nums))
# print(list(map))
# filter = list(filter(lambda x:x%2==0,nums))
# print(filter)


'''ATM AND CALCULATOR'''

'''ATM PROGRAM'''
# def atm(x,y):
#     amount = 1000
#     if name == username and password == passwords:
#         while True:
#             print(s)
#             option = int(input("Enter the option:"))
#             if option == 1:
#                 credit_amount=float(input("Enter the Amount:"))
#                 print("Amount after credit:",amount+credit_amount)
#             elif option == 2:
#                 debit_amount=float(input("Enter the debit amount:"))
#                 print("Amount after debit:",amount-debit_amount)
#             elif option == 3:
#                 print("mini statement Amount:",amount)
#             elif option == 4:
#                 print("thank you")
#                 break
#             else:
#                 print("Incorrect")
# name = "varma"
# password = "123"
# username = input("Enter the User Name:")
# passwords = input("Enter the Password:")
# s = '''       1.Credit
#        2.Debit
#        3.Mini statement
#        4.Exit'''
# atm(username,passwords)


'''CALCULATOR'''

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def inp():
#     a = float(input("Enter the first number:"))
#     b = float(input("Enter the second number:"))
#     return a,b

# s = '''OPERATIONS
# 1.addition
# 2.subtraction
# 3.multiplication
# 4.division'''

# while True:
#     print(s)
#     option = int(input("Enter your option:"))
#     if option == 1:
#         c = inp()
#         print("addition:",add(c[0],c[1]))
#     elif option == 2:
#         c = inp()
#         print("subtraction:",sub(c[0],c[1]))
#     elif option == 3:
#         c = inp()
#         print("multiplication:",mul(c[0],c[1]))
#     elif option == 4:
#         c = inp()
#         print("division:",div(c[0],c[1]))
#     else:
#         print("invalid option")