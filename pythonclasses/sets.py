sunny={3,53,4,23,514,6134,1,5,321}
# print(type(sunny))

# sunny[0]=12

# print(sunny[0])

print(sunny)

sunny = {1,1,1,2,2,2,3,4,53,546,4}
print(sunny)

''' SET METHODS'''

sunny = {1,1,1,2,2,2,3,4,53,546,4}
sunny.add(123)
print(sunny)

sunny.add(1)
print(sunny)

sunny.update({1,2,3,4,5,6,7,8,9,0})
print(sunny)

sunny.remove(546)       #particular element is removed
print(sunny)

sunny.pop()               #Random element is removed
print(sunny)

vimath = {3,2,1,4}
# print(vimath.clear())

vimath.clear()
print(vimath)

vimath = {3,2,1,4}
sandeep = vimath.copy()
vimath.add(22)
print(vimath)
print(sandeep)


'''Set operations'''

set1 = {1,2,3,4,5}
set2 = {5,6,7,8,4}
# print(set1.union(set2))

print(set1.intersection(set2))

set1 = {1,2,3}
set2 = {5,6,7,2}
# print(set1.difference(set2))

print(set1.symmetric_difference(set2))

set1={1,2,3}
set2={5,6,7}
print(set1.isdisjoint(set2))

set1 = {1,2,3,4,5}
set2 = {1,2,3}
# print(set1.issubset(set2))

# print(set2.issubset(set1))

print(set1.issuperset(set2))

for j in {1,2,3,4,5,45}:
    if j==1:
        print("yes")
        break
    else:
        print("false")


'''FROZEN SET'''

h = [12,33,44,4]
print(type(h))
d = frozenset(h)
print(type(d))
# d.append(123)

print(d)




