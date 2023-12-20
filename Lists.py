mylist = ['surya',50,'job','miyapur']
print(mylist[0:5])

thislist = ["surya", "banana", "cherry"]
if mylist[0] in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print('No sorry')

mylist.insert(1,'hai')
print(mylist)  

x = 'hai1'

if x in mylist:
    mylist.remove(x)
else:
   mylist.insert(2,'pose')    


print(mylist)