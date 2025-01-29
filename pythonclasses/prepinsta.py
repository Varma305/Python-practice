# # 1)Find the Sum of The First N Natural Numbers in Python

# '''METHOD 1 USING FOR LOOP'''

# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum = sum + i
# print(sum)

# '''METHOD 2 USING RECURSION'''

# def getsum(num):
#     if num == 1:
#         return 1
#     return num + getsum(num-1)

# num = int(input())
# print(getsum(num))

#2)Find the Sum of the Numbers in a Given Range

# #method 1

# a = int(input())
# b = int(input())
# sum = 0
# for i in range(a,b+1):
#     sum = sum+i
# print(sum)

# #method 2

# def getsum(a,b):
#     if b>=a:
#         if b == a:
#             return a
#         return b + getsum(a,b-1)
#     else:
#         return 0

# a = int(input())
# b = int(input())
# print(getsum(a,b))

# def recursum(sum,num1,num2):
#   if num1 > num2:
#     return sum
#   return num1 + recursum(sum,num1+1,num2)

# num1, num2 = 6, 3
# sum = 0
# print(recursum(sum,num1,num2))

# #3) leap year

# def checkyear(year):
#     return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

# year = int(input())
# if checkyear(year):
#     print("leap year")
# else:
#     print("not a leap year")

# #4) prime number

# num = int(input())
# flag = 0
# for i in range(2,num):
#     if num%i == 0:
#       flag = 1
#       break
# if flag == 1:
#    print("not prime")
# else:
#    print("prime")

# num = int(input())
# def checkprime(num,i=2):
#   if num==i:
#     return True
#   if num%i==0:
#     return False
#   if num<2:
#     return False
#   return checkprime(num,i+1)
# if checkprime(num)==True:
#   print("prime")
# else:
#   print("not prime")


#5) Find the sum of the Digits of a Number

# # num = int(input())
# # sum = 0

# # while num!=0:
# #     digit = int(num%10)
# #     num = num/10
# #     sum += digit
# # print(sum)

# num = input()
# sum = 0

# for i in num:
#     sum = sum + int(i)
# print(sum)

# num = int(input())
# sum = 0

# def findsum(num,sum):
#     if num == 0:
#         return sum
#     digits = int(num%10)
#     sum += digits
#     return findsum(num/10,sum)
# print(findsum(num,sum))



'''Positive or Negative number'''


# num = int(input())
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")


'''Even or Odd number'''

# num = int(input())

# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")


'''Sum of First N Natural numbers'''

# num = int(input())
# sum = 0
# for i in range(num+1):
#     sum += i
# print(sum)

'''Greatest of two numbers'''

# num1 = int(input())
# num2 = int(input())

# if num1 > num2:
#     print(f"{num1} is greater")
# else:
#     print(f"{num2} is greater")

##using inbuilt function

# num1 = int(input())
# num2 = int(input())

# print(max(num1,num2))


''''''
