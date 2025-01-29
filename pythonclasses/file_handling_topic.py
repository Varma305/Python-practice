'''FILE HANDLING'''

file = open("demo.txt",mode = "r")
c = file.read()
# c = file.readline()
# c = file.readlines()
print(c)
file.close

file = open("demo.txt",mode = "r")
c = file.read(7)
print(c)
file.close

file = open("demo.txt",mode = "w")
c = file.write("this is my write function")
file.close()

file = open("demo.txt",mode="a")
c = file.write("\nthis is my append mode")
file.close()

# Reading file in 'r+' mode

with open('demo.txt','r+') as fd:
    print(fd.tell())
    print(fd.read())
    print(fd.tell())

# Reading file in 'w+' mode

with open('demo.txt','w+') as fd:
    print(fd.tell())
    print(fd.read())
    print(fd.tell())
    c = fd.write("this is w+")

with open('demo.txt','w+') as fd:
    print(fd.tell())
    c = fd.write("this is w+")
    print(fd.read())
    print(fd.tell())
    
# write file in r+ mode
 
with open('demo.txt','r+') as fd:
    fd.write("new text.")

with open('demo.txt','w+') as fd:
    fd.write("new text.")

# opening file in 'w+' mode when it does not exist

with open('sample1.txt','w+') as fd:
    pass

fp = open("demo.txt",'r')
print(fp.tell())
fp.read()
print(fp.tell())
fp.seek(0)
print(fp.tell())
fp.close()


file = open('demo.txt',mode='r+')
content = file.read()
v = str(content)
print(v)
f=v.split()
print(f)
f.insert(2,'chetan')
print(file.tell())
file.close()
file = open('demo.txt',mode = 'w')
print(f)
for i in f:
    file.writelines([i])


'''ERROR HANDLING'''

try:
    print(a)
except:
    print("error vachindi")
else:
    print("error raledu")
finally:
    print("always")

try:
    print('a')
except:
    print("error vachindi")
else:
    print("error raledu")
finally:
    print("always")

try:
    print('a'+10)
except:
    print("error occured")

try:
    print('a'+10)
except Exception as kiran:
    print("error occured",kiran)

try:
    print('a'+10)
except TypeError:
    print("type error occured")
except NameError:
    print("name error occured")

try:
    print('a'+10)
except:
    print("outer")
    try:
        print(a)
    except:
        print("inner")

