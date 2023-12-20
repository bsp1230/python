thisdict = {
  "brand": "Ford",
  "model": "Tata",
  "year": 1964
}

print(thisdict)
books = {'name':'Alchemist','author':'surya','year2':2023}
print(books['author'])
books['price']=450.0
print(books)
print(books.items())
#Removing items
books.pop('year2')
print(books)
for x,y in books.items():
    print(x,':',y)
x = dict(books)
print(x)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
for x in books:
    if books[x]=='xx':
        print('yes')
    else:
        print('no')    
