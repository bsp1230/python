x, y, z = "Orange", "Banana", "Cherry"
print(x+y+z)
print(y)
print(z)
firstName = 'surya';
print(firstName)


x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = ("apple", 'banana', "cherry")
x, y, z = fruits
print(x)
print(y)
print(z)


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)





x = "awesome"

def myfunc():
  global x
  #x = "fantastic"

myfunc()

print("Python is " + x)



x = 5
print(type(x)) 