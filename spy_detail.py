from datetime import datetime



                              #define class
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name                     #name
        self.salutation = salutation         #salutation
        self.age = age                       #age
        self.rating = rating                 #ratting
        self.is_online = True                #user is online
        self.chats = []
        self.current_status_message = None    #checck there is any status or not


                                  #define class
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message                         #self message
        self.time = datetime.now()                     #form datetime fxn
        self.sent_by_me = sent_by_me


spy = Spy('shubham', 'Mr.', 24, 4.7)                    #main user

friend_one = Spy('arnav', 'Mr.', 4.9, 27)               #first friend
friend_two = Spy('sahil', 'Ms.', 4.39, 21)              #second friend
friend_three = Spy('rajiv', 'Dr.', 4.95, 37)             #third freind

friends = [friend_one, friend_two, friend_three]         #enter all friend in list


                          #user detail of old user
spy_name="shubham"
spy_salutation="mr." +" " +spy_name +" welcome again"
spy_age="your age =19"
spy_ratting="your old ratting=4.5"


                 #user detail  for new user
a=raw_input("what is ur name")
b=raw_input("what i called u mr. or miss")
print'welcome' + ' ' +b +a + ' to spychat'
c=raw_input("what is ur age")
print type(c)
c=int(c)
if c>16 and c<45:
          d=raw_input("may i know what is ur rating")
          d=float(d)
          if d>4.5:
              print"great"
          elif d>3.5 and d<=4.5:
              print"better"
          elif d>2.5 and d<=3.5:
              print"gud"
          elif d>1.5 and d<=2.5:
              print"bad"
          elif d>1 and d<=1.5:
              print"fuddu"
else:
          print("you r not in the the age group")