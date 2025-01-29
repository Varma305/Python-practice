# py_dict={1:'apple',2:"oneplus"}
# print(type(py_dict))
# print(py_dict)


# sunny={"kiran":"names","sno":2.2,11:True}
# print(sunny)
# print(sunny["kiran"])
# print(sunny["sno"])
# print(sunny[11])
# sunny["kiran"]="python"
# print(sunny)    


'''dictionary methods'''
# sunny={"sno":1,"name":"sunny","phone":[12,32]}

# print(sunny.get("sno"))
# print(sunny.get("name"))
# print(sunny.get("phone"))

# print(sunny.keys())

# print(sunny.values())

# print(sunny.items())


# sunny.update({"food":"biryani"})
# print(sunny)

# sunny.pop("sno")
# print(sunny)

# print(list(sunny))


'''tuple'''

# mohan=(1,22,2,232.33)
# print(mohan[1])
# mohan[0]="kiran"
# print(mohan)

'''bulit in functions'''

# mohan=(1,22,2,232.33)
# print(max(mohan))
# print(min(mohan))
# print(sum(mohan))
# print(len(mohan))
# print(list(mohan))

'''tuple operations'''

# t1=(1,2,3)
# t2=(4,5,6)
'''concatentation'''
# print(t1+t2)   
# new=[]
# for i,j in zip(t1,t2):
#     new.append(i+j)
# print(tuple(new))

# d=(1,2,3)
# print(d*5)

# d=(2,3,4,5,6,6,7,7,87,88,8)
# print(22 not in d)

# t1=(1,2,3)
# t2=(1,2,3,5,35,34,)
# print(t1 is not t2)



# d=(1,5,9,3,5,7,6,4)
# for i in d:
#     print(i)



'''ATM program'''


# name="varma"
# password="0000"
# user_name=input("Enter the name:")
# passwords=input("Enter the password:")
# s='''
#     1.Credit
#     2.Debit
#     3.Mini statement
#     4.Exit

#   '''
# amount=1000
# if name==user_name and password==password:
#      while True:
#         print(s)
#         option=int(input("Enter the option:"))
#         if option==1:
#             credit_amount=float(input("Enter the amount:"))
#             print("Amount after credit:",amount+credit_amount)
#         elif option==2:
#             debit_amount=float(input("Enter the amount:"))
#             print("Amount after debit:",amount-debit_amount)
#         elif option==3:
#             print("###Mini Statement Amount###:",amount)
#         elif option==4:
#             break

# else:
#     print("Incorrect")

