'''1) python program to check a number is positive or negative or zero'''

# num = float(input("Enter the num:"))
# if num > 0:
#     print("positive number")
# elif num == 0:
#     print("zero")
# else:
#     print("negative number")

'''2) leap year'''

# def checkyear(year):
#     return (((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0)

# year = int(input("Enter a year:"))
# if(checkyear(year)):
#     print("leap year")
# else:
#     print("not a leap year")

'''3) Largest among 3 numbers'''

# num1 = float(input("Enter the number:"))
# num2 = float(input("Enter the number:"))
# num3 = float(input("Enter the number:"))

# if (num1>=num2) and (num1>=num3):
#     largest=num1
# elif (num2>=num3) and (num2>=num1):
#     largest=num2
# else:
#     largest=num3
# print("largest number is:",largest)

'''4) prime or not '''

# def is_prime(number):
#     if number>1:
#         for num in range(2,number):
#             if number%num == 0:
#                 return "not a prime"
#         return "prime"
#     return "not a prime"

# d = int(input("enter the number:"))
# print(is_prime(d))

'''5) even number or odd'''

# def is_even(num):
#     if num%2 == 0:
#         return "even"
#     return "odd"

# d = int(input("Enter the number:"))
# print(is_even(d))

'''6) Find the Number is Armstrong or Not '''

# n=int(input("Enter the number:"))
# s=n     #temporary variable to store 
# l=len(str(n))
# sum=0
# while n!=0:         #153!=0         15!=0               1!=0
#     r=n%10          #153%10=3       15%10=5             1%10=1
#     sum=sum+(r**l)  #0+(3**3)=27    27+(5**3)=27+125    152+(1**3)
#     n=n//10         #153//10=15     15//10=1            1//10=0
# if s==sum:
#     print("Armstrong number")
# else:
#     print("not a amstrong number")


'''7) palindrome program'''

# def ispalindrome(s):
#     return s == s[::-1]

# s = input("Enter the value:")
# ans = ispalindrome(s)

# if ans:
#     print("palindrome")
# else:
#     print("Not a palindrome")


n = int(input("Enter the number:"))
s = n
l = len(str(n))
sum = 0
while n!=0:
    r = n%10
    sum = sum + (r**l)
    n = n//10

if s == sum:
    print("Armstrong")
else:
    print("Not a Armstrong")