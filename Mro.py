#Inheritance
#Single Inheritance
'''class parent:
     def fun(self):
        print("Parent class")
class child(parent):
    def fun2(self):
        print("Child class")
obj=child()
obj.fun()
obj.fun2()'''


'''class student:
    def details(self):
        self.name=input("Enter your name:")
        self.roll_no=int(input("Enter your roll no:"))
        self.div=input("Enter your division")
        print("Student Name is {} and his roll no is {} and he is from {} division".format(self.name,self.roll_no,self.div))
class percentage(student):
    def marks(self):
        self.m1=int(input("Enter your Engish:"))
        self.m2=int(input("Enter Science:"))
        self.m3=int(input("Enter Math:"))
        avg=(self.m1+self.m2+self.m3)/3
        if avg>35:
            print("Pass")
        else:
            print("Fail")
        print("Average of studens is {}:".format(avg))
        print("Student {} is pass by percentage {}".format(self.name,avg))
obj=percentage()
obj.details()
obj.marks()'''



#Multilevel Inheritance:

'''
class login:
    def __init__(self):
        self.username="Admin"
        self.passward="Admin@123"
class homepage(login):
    def cheaklogin(self):
        self.username1=input("Enter username:")
        self.passward2=input("Enter your passward:")
        if self.username==self.username1:
            if self.passward==self.passward2:
                print("Welcome to homepage")
            else:
                print("incorrect pass")
        else:
            print("Incorrect username")
class signout(homepage):
    def timeout(self):
        print("Timeout")
obj =signout ()
obj.cheaklogin()
obj.timeout()



'''







'''class object:
    def m1(self):
        print("in m1 of object")

class O():
    def m1(self):
        print("in m1 of o")
class D(O):
    def m1(self):
        print("in m1 of d")
class E(O):
    def m1(self):
        print("in m1 of E")
class F(O):
    def m1(self):
        print("in m1 of F")
class B(D,E):
     def m1(self):
         print("in m1 of B")
class C(D,F):
    def m1(self):
       print("in m1 of C")
class A(B,C):
    def m1(self):
        print("in m1 of A")

print(A.mro())
print(C.mro())
print(B.mro())
print(F.mro())
print(E.mro())
print(D.mro())'''
import threading

'''class o():
    def m1(self):
        print("m1 in o")
class c(0):
    def m1(self):
        print("m1 in c")
class a(0):
    def m1(self):
        print("m1 in a")
class b(o):
    def m1(self):
        print("m1 in o")
class d(o):
    def m1(self):
        print("m1 in d")
class k1(o):
    def m1(self):
        print("m1 in o")
class o():
    def m1(self):
        print("m1 in o")
class o():
    def m1(self):
        print("m1 in o")'''
# Super Method
'''class oops:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self,other):
        temp=[self.x+other.x,self.y+other.y,self.z+other.z]
        return oops ( temp[0],temp[1],temp[2])
    def __str__(self):
     return str(f"{self.x},{self.y},{self.z}")
obj=oops(1,2,3)
obj1=oops(1,2,3)
obj2=oops(1,2,3)
print(obj+obj1+obj2)'''

#Abstraction
'''
from abc import ABC,abstractmethod
class emp(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class Infemp(emp):
    def m1(self):
        print("In m1")
class Inemp(Infemp):
    def m2(self):
        print("In m2")


object=Inemp()
object.m1()
object.m2()'''


#Access Specifier
# Public=p
# protected=_p  (Use in parent and immediate inherit clss)
# Private=__p (Use within the clss)
'''
class sp:
    public=100
    _protectd=200
    __private=400
class b(sp):
    print("Public",sp.public)
    print("Public", sp._protectd)
 #  print("Public", sp.private) (Cannot use in second clss)

obj=b()
print("Private ",obj._sp__private)   #We can use private variable outside the class by using name manglling

'''
#Modules

'''def mro():
   print(" in mro")
def mro2():
   print(" in mro2")
def mro3():
   print(" in mro3")'''


'''class login:
   def __init__(self):
      self.username = "Admin"
      self.passward = "Admin@123"
object=login()'''

#File Handling:-

'''fp=open("demoemail.txt",'r')
print(fp.read())'''  #---read()

'''fp=open("test.txt",'r')
print(fp.readlines())'''  #----readlines()



'''fp=open("test.txt",'w')
print(fp.write(''Dear Trupti, Thank you for registering. As the first step in the recruitment process, Accolite Digital would like you to take the online assessment on EduThrill.''))
'''   #-----Write

'''fp=open("test.txt",'w')
print(fp.writelines("HII\n","hello\n"))'''

'''fp=open("test.txt",'a')
fp.write("\nHello everyone How are you")'''  #----append



#r+  (First reads and then write)


'''fp=open("test.txt","r+")
fp.read()
fp.write("Hello everyone%%%%%%%%")'''

#w+    (First Write and then read)

'''fp=open("test.txt","w")
fp.write("Dear Trupti, Thank you for registering. As the first step in the recruitment process, Accolite Digital would like you to take the online assessment on EduThrill.")
'''

'''fp=open("test.txt","w+")
fp.write("Hello everyone")
fp.read()'''


# a+ (First apend and then write)
'''fp=open("test.txt",'a+')
fp.write("Dear Trupti, Thank you for registering. As the first step in the recruitment process, Accolite Digital would like you to take the online assessment on EduThrill.")
fp.read()'''



# x---Exclusive Mode (if file is present then gives error if not present then creats new file)

'''fp=open("test.txt",'x')
fp.write("HIIIIIIIIIIII")'''


'''with open("test.txt",'w') as fp:
    fp.write("Hi everyone???")'''



'''with open("test.txt",'w') as fp:
    fp.write("hii")

    print(fp.closed)
print(fp.closed)'''

'''import csv
with open("test.csv",'r') as fp:
    r=csv.reader(fp)
    print(list(r))'''

'''
import csv
with open("test.csv",'w') as fp:
    w=csv.writer(fp)
    w.writerow(['name','age','sal'])
    count=int(input("Enter the row count:--"))
    for i in range (count):
        name=input("enter  a name:--")
        age=input("Enter a age:---")
        sal=input("Enter a sal:--")
        w.writerow([name,age,sal])
'''


#dict to binary (Serialization)

'''import pickle
my_dict={
    'name':'Raj',
    'age':12,
    'id':111
}
with open('file12.txt','wb')as fp:
    data=pickle.dump(my_dict,fp)
    print(data) '''
import json

#binary to dict (Deserialization)
'''import pickle
with open('file12.txt','rb') as fp:
    data=pickle.load(fp)
    print(data)'''


#Dict to JSON
# dumps() -- dict to json stirng

'''d={
    'name':'raj',
    'age':23,
    'id':101
}
js=json.dumps(d)
print(js)
'''

#dump()-- dict to JSON and store in file

'''d={
    'name':'Rahul',
    'id':11111,
    'age':233
}
with open('file12.txt','w') as fp:
    data=json.dump(d,fp)
    print(data)'''

#Json to dict
'''import json
with open('file12.txt','r')as fp:
    data=json.load(fp)
    print(data)'''


d={
    'name':"rahul",
    'id':222
}



#dict to Yaml





#OS module

'''import os            #Current directory
print(os.getcwd())'''


'''import os           #Change directory
print(os.chdir(rTrupti Kondhare\PycharmProjects\pythonProject"))
'''

'''import os      #Make single directory
os.mkdir("test123.py")
'''


'''import os            #Remove directory
os.rmdir("test123.py")
'''


'''import os           #Make multiple directories
os.makedirs(r"k1\k2\k3")'''


'''import os        #To remove multiple directories
os.removedirs(r"k1\k2\k3")'''






#Multithreading

'''
import threading
print(threading.current_thread())

'''

 #Creating thread without using class(Function Based)


'''def qube():
     for i in range(1,11):
         print(i**3)
t1=threading.Thread(target=qube())
t1.start()
for j in range(1,13):
      print(j)
for k in range(1,20):
    print(k**2)
    '''


#Creating thread by thread class
'''
from threading import Thread
class test(Thread):
    def run(self) :
        for i in  range(1,29):
            print("In child Thread")
obj=test()
obj.start()
obj.join()          #join will wait to execution of child class after main class will execute
print("In main thread")
'''

#Creating thread without extending thread class

'''
from threading import Thread

class test():
    def m1(self):
        for i in range(1,22):
            print(i)
    def m2(self):
        for j in range(22,40):
            print(j)
obj=test()
t1=Thread(target=obj.m1())
t2=Thread(target=obj.m2())
t1.start()
t2.start()
t1.join()
t2.join()
print("Main Thread")

'''


#Logging
'''
Critical 50
error 40
warning 30
info 20
debug 10
'''

import logging
logging.basicConfig(filename="server.log",level=10,filemode='w',format='%(asctime)s-%(levelname)s-%(message)s',datefmt='%y:%m:%d %I:%M:%S %p')
logging.critical("Condition of program is critical")
logging.error("Condition of program is error")
logging.warning("Condition of program is warning")
logging.info( "Condition of program is info")
logging.debug("Condition of program is debug")