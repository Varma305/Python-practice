# varma=[]
# print(type(varma))

# varma=list()
# print(type(varma))

# varma=[1,2.2,'python',True]
# varma1=list([1,2.2])
# print(varma)
# print(varma1)

# sandeep=[2.2,3.4,5.5,1,2,3,4,5]
# print(sandeep[-1])

# james_bond=[7,3,5,3,34,64,2.4,32,5,35,35]
# print(james_bond[0:5+2])
# print(james_bond[:5])
# print(james_bond[5:])
# print(james_bond[::])
# print(james_bond[:])
# print(james_bond[:-1])
# print(james_bond[::-1])


# james_bond=[7,3,5,3,34,64,2.4,32,5,35,35]
# james_bond[5]="varma"
# james_bond[8]="varma"
# print(james_bond)

'''list methods'''

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.append([123])
# print(varma)


# varma=[1,2,3,4,4525,23,63,63,6]
# varma.extend([123])
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# print(varma.count(63))


# varma=[1,2,3,4,4525,23,63,63,6]
# print(varma.index(4525))

# varma=[1,2,3,4,4525,23,63,63,6]
# print(len(varma))

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.clear()
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# b=varma.copy()
# varma.append('abc')
# print(b)
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.insert(0,123)
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.pop(1)
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.remove(2)
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.reverse()
# print(varma)

# varma=[1,2,3,4,4525,23,63,63,6]
# varma.sort(reverse=True)
# print(varma)

'''list compherension'''

# new=[x**2 for x in [1,2,3,4,5]]
# print(new)

# list=["even" if i%2==0 else "odd" for i in range(10)]
# print(list)

# for i in range(10):
#     if i%2 == 0:
#         print("even",end=" ")
#     else:
#         print("odd",end=" ")

# fruits=["apple","banana","cherry","mango"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)

# newlist=[]
# for i in ["apple","banana","cherry","mango"]:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)


# s=[1,2,3,4,3,4]
# for i in range(len(s)):
#     if s[i]==4:
#         print(i)

# str1=[1,6,6,6,6,6,2,4,5,6,3]
# n=[]
# for i in str1:
#     if i==6:
#         str1.remove(6)
#     else:
#         n.append(i)
# print(n)