#OOP's

# class suraj:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(self.name)

# r = suraj("hello")
# r.show()


#eg - 2
# class suraj:
#     def __init__(self):
#         print("calling constructor")

#     def show(self):
#         print("show the name : ")

# r = suraj()
# r.show()


#eg - 3
# class suraj:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getAge(self):
#         print("My age is : ",self.age)

#     def getName(self):
#         print("My name is : ",self.name)

# s = suraj("hello", 20)
# s.getAge()
# s.getName()

# s = suraj(age = 20, name = "hello")
# s.getAge()
# s.getName()



# # eg -> 4
# class student:
#     def __init__(self, *args):
#         print(type(args))
#         print(args)
#         self.name = args[0]

#     def getStu(self):
#         # print("the student is :", self.name)
#         return self.name

# s = student("hello", 20, "000000000", "suraj@gmail.com")
# t = s.getStu()
# print(t)



# question
# class student:
#     def __init__(self,args):
#         print(type(args))
#         print(args)
#         self.name = args

#     def getStu(self):
#         # print("the student is : ",self.name)
#         return self.name

# s = student({"name":"hello", "age":20}) 
# t = s.getStu()
# print(t["age"])


#Eg -> 5
# class student:
#     def __init__(self,*args):
#         self.data = args

#     def users(self):
#         print(self.data[0])
#         print(self.data[1])
#         print(self.data[2])


#     def details(self):
#         print("Address :",self.data[1][0])
#         print("college :",self.data[1][1])
#         print("location :",self.data[1][2])


# s = student(["suraj", "sushant", "Deepak", "shivam"],{"address":"kukas", "college":"arya", "location":"jaipur"})
# t = s.users()
# u = s.details()

# print(t)
# print(u)



# class student:
#     def __init__(self,*args):
#         self.data = args

#     def users(self):
#         for i in self.data[0]:
#             print(i)


#     def details(self):
#         print(self.data[1])
#         for i in self.data[1]:
#             print()



# s = student(["suraj", "sushant", "Deepak", "shivam"],{"address":"kukas", "college":"arya", "location":"jaipur"})
# s.users()
# s.details()



# class student:
#     def __init__(self, **args):
#         print(type(args))
#         print(args)
#         self.data = args

#     def data(self):
#         print(self.data["name"])

# s = student(name = "hello", age = 20, user = ["a", "b", "c"])
 



# class Address:
    # city = "jaipur"
    # state = "Rajasthan"
#     def __init__(self,city,state): #this -> self
#         self.city = city #attribute
#         self.state = state

# a = Address("jaipur" , "Rajasthan")
# print(a.state)


# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def show(self): #method
#         print("the city is : ",self.city)

# a = Address("jaipur","rajasthan")
# a.show()   