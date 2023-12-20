def f1(x,y):
      print("Hello from a function",x)

f1('xyz',96);

def courses(*skills):
      print(skills)

courses('java','cse','eee')


def countries(country = "Norway"):
  print("I am from " + country)

def randomNo(i):
     return i * round(i);

print(randomNo(95));


def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
recursion(10);

def myfunc(n):
  return lambda a : a * n
x = myfunc(81)
print(x(96));