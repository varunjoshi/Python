floor1 =[]
floor2=[]
floor3=[]
#increse or decrease numbers as per need.
members1=2
members2=2
members3=2

for i in range (members1):
   name = input("Enter name of First floor member: ")
   age = int(input("Enter age: "))
   floor1.append(name)
   floor1.append(age)
  

for j in range (members2):
     name = input("Enter name second floor member:: ")
     age = int(input("Enter age: "))
     floor2.append(name)
     floor2.append(age)
  


for k in range (members3):
     name = input("Enter name third floor member:: ")
     age = int(input("Enter age: "))
     floor3.append(name)
     floor3.append(age)


floordetails = int(input("Enter floor details needed: "))
if floordetails == 1:
    print("Floor 1 members:", floor1)
elif floordetails == 2:
    print("Floor 2 members:", floor2)
elif floordetails == 3:
    print("Floor 3 members:", floor3)
elif floordetails != 1 or 2 or 3 :
     print("Please choose only from 1,2 or 3")



