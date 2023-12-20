thisset = {"apple", "banana", "cherry", "apple",'cherry',True,1}

print(thisset)

x1 = thisset.copy()
print(x1)

thisset = tuple(("apple", "banana", "cherry",'surya'))
print(thisset)
x2 = x1.update(thisset)
print(x2)

if 'surya' in x1:
    print('yes')
else:
    print('no')    

print(x1.union(thisset))
