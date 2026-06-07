#INHERITANCE

# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state 

#     def location(self):
#         return f"my location is {self.city} in {self.state}"
    
# class User(Address):
#     def __init__(self,name,age,city,state):
#         super().__init__(city,state)
#         self.name = name
#         self.age = age
#         # self.city = city #super()
#         # self.state = state
#     def userName(self):
#         print(f"my name is {self.name}")

    
#     def userDetails(self):
#         print(f"my name is {self.name} and my location is {self.city} in {self.state}")


# u = User("suraj", 20, "kukas", "rajasthan")
# print(u.city)
# u.userDetails()
# u.location()

# a = Address("kukas", "rajasthan")






#Encapsulation
# class Address:
#     def __init__(self,city,state):
#         self.__city = city #private attribute
#         self.state = state #attribute

#     def location(self):
#         print(f"my location is {self.__city} in {self.state}")

#     def get_city(self):
#         return self.__city

# a = Address("patna", "Bihar")
# a.location()
# a.get_city()
# # print(a.__city) #
# print(a.state)





#Polymorphism
# class Address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
    
#     def location(self):
#         print(f"my address location is {self.city} in {self.state}")

# class HomeTown:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state

#     def location(self):
#         print(f"my home town location is {self.city} in {self.state}")


# a = Address("vadodara","gujrat")
# a.location()
# b = HomeTown("Patna","Bihar")
# b.location





# class Address:
#   def __init__(self,city,state):
#     self.city = city
#     self.state = state
#   def location(self):
#     print(f"my address location is {self.city} in {self.state}")
 
# class HomeTown:
#   def __init__(self,city,state):
#     self.city = city
#     self.state = state
 
#   def location(self):
#     print(f"my home town location is {self.city} in {self.state}")
  
# a = Address("vadodara","gujrat")
# a.location()
# b = HomeTown("chappra","bihar")
# b.location()




#class variables

# class Address:
#   total = 10 #class variable
#   def __init__(self,city,state):
#     self.city = city 
#     self.state = state
#     Address.total += 1

#     def location(self):
#       print("location")

# a = Address("jaipur", "rajasthan")

# b = Address("patna" , "rajasthan")

# a.total


#overloading and overriding

# def address(city,state):
#     print(f"my address is {city} in {state}")

# def address(city,state,country):
#     print(f"my address is {city} at {state} in {country}")

# # address("patna", "bihar")  #overloading possible ni hai 
# address("jaipur", "rajasthan", "india")


# class Address:
#   def __init__(self,city,state):
#     self.city = city
#     self.state = state
#   def location(self):
#     print()