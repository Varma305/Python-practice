'''oops - object oriented programming language based on objects(data,code)
    where data--variable and code--functions
    class,object,abstraction,inheritance,encapsulation,polymorphism'''


# class varma():
#     def output():
#         print("this is class")
#     output()   



# class varma():         
#     def output(self):
#         print("this is class")
# # object creation --->object name = class name()
# vivo = varma()        # object is created
# vivo.output()         # methods access-->objectname.method



# class varma():          # class defination
#     a = 10              # attribute
#     def sunny(self):    # method
#         print("this is sunny")
# lrv = varma()           # object creation
# print(lrv.a)            # objectname.variable
# lrv.sunny()             # objectname.method


# class varma():
#     a = 10
#     def classmethod(self):
#         print("this is class")
# sunny1 = varma()
# sunny = varma()
# sunny1.classmethod()
# sunny.classmethod()
# print(sunny.a)



# class varma():
#     a = 10
#     def output(self):
#         print(self.a)
# obj = varma()
# obj.output()


# class Naveen():
#     a = 10
#     def display(self):
#         print(self.a)

# ram = Naveen()
# syam = Naveen()
# ram.display()
# syam.display()


'''constructors'''

# class prakesh():
#     def __init__(self,a,b,c):
#         self.ff=a
#         self.vv=b
#         self.dd=c
#     def output(self):
#         print(self.ff,self.vv,self.dd)
# p=prakesh(1,2,3)
# p.output()

# class prakesh():
#     def __init__(self,a,b,c):
#         self.ff=a
#         self.vv=b
#         self.dd=c
#         print(a)
#     def output(self):
#         print(self.ff,self.vv,self.dd)
# p=prakesh(1,2,3)
# p.output()


# class mobiles():
#     def __init__(self,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         self.a=mobile_name
#         self.b=mobile_ram
#         self.c=mobile_battery
#         self.d=mobile_price
#     def mobile_data(self):
#         print("mobile name:",self.a)
#         print("mobile ram:",self.b)
#         print("mobile battery:",self.c)
#         print("mobile price:",self.d)

# mobile_obj=mobiles("apple","8gb","6000mah","40000")
# mobile_obj.mobile_data()


# class mobiles():
#     def __init__(self,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         self.a=mobile_name
#         self.b=mobile_ram
#         self.c=mobile_battery
#         self.d=mobile_price
#     def mobile_data(self):
#         print("mobile name:",self.a)
#         print("mobile ram:",self.b)
#         print("mobile battery:",self.c)
#         print("mobile price:",self.d)
# name=input("Enter the mobile name:")
# ram=input("Enter the mobile ram:")
# battery=input("Enter the mobile battery:")
# price=float(input("Enter the mobile price:"))

# mobile_obj=mobiles(name,ram,battery,price)
# mobile_obj.mobile_data()

# class mobiles():
#     def __init__(self,mobile_name,mobile_ram,mobile_battery,mobile_price):
#         self.a=mobile_name
#         self.b=mobile_ram
#         self.c=mobile_battery
#         self.d=mobile_price
#     def mobile_data(self):
#         print("mobile name:",self.a)
#         print("mobile ram:",self.b)
#         print("mobile battery:",self.c)
#         print("mobile price:",self.d)
# while True:
#     name=input("Enter the mobile name:")
#     ram=input("Enter the mobile ram:")
#     battery=input("Enter the mobile battery:")
#     price=float(input("Enter the mobile price:"))

#     mobile_obj=mobiles(name,ram,battery,price)
#     mobile_obj.mobile_data()



'''DAY - 2'''

'''INHERITANCE'''

# class parent:               #single inheritance
#     def output(self):
#         print('this is parent class')
# class child(parent):
#     def childoutput(self):
#         print('this is child class')
# i = child()
# i.output()
# i.childoutput()


# class Father:                   #multiple inheritance
#     def output(self):
#         print('this is parent class')
# class mother:
#     def outputm(self):
#         print('this is mother class')
# class child(Father,mother):
#     def outputchild(self):
#         print('this is child class')
# i=child()
# i.output()
# i.outputm()
# i.outputchild()


# class Grandfather:
#     def output(self):
#         print('this is grand father class')
# class Father(Grandfather):
#     def outputf(self):
#         print('this is father class')
# class child(Father):
#     def outputchild(self):
#         print('this is child class')
# i=child()
# i.output()
# i.outputf()
# i.outputchild()


# class Father():
#     def output(self):
#         print('this is father class')
# class child1(Father):
#     def outputf(self):
#         print('this is child 1 class')
# class child2(Father):
#     def outputchild(self):
#         print('this is child 2 class')
# ice = child1()
# cream = child2()
# ice.output()
# ice.outputf()
# cream.output()
# cream.outputchild()


'''polymorphism'''

# #method overload

# class methodoverlod:
#     def something(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj = methodoverlod()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)
# obj.something()

# #method overridding

# class methodoverri:
#     def display(self):
#         print("this is parent class")
# class child(methodoverri):
#     def display(self):
#         print("this is child class")
# obj=child()
# obj.display()

# class methodoverri:
#     def display(self):
#         print("this is parent class")
# class child(methodoverri):
#     def display(self):
#         print("this is child class")
#         super().display()
# obj=child()
# obj.display()


'''encapsulation'''

# class Gfather:                  #protected 
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class Father(Gfather):
#     def display1(self):
#         print(self._y)
# class child(Father):
#     def display2(self):
#         print("child",self._y)
# obj = child(12)
# obj.display2()
# obj.display1()


# class Gfather:                  #private 
#     def __init__(self,a):
#         self.__y=a
#         print(self.__y)
# class Father(Gfather):
#     def display1(self):
#         print(self.__y)
# class child(Father):
#     def display2(self):
#         print("child",self.__y)
# obj = child(12)
# obj.display2()
# obj.display1()


'''abstraction'''

