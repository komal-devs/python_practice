numbers = [1,2,3,4,5,6,7,8]
even = []
for i in numbers :
  if i%2 == 0:
    even.append(i)
print(even)

# with list comprehension
numbers = [1,2,3,4,5,6,7,8]
even = [i for i in numbers if i%2 == 0]
print(even)

# zip() - take inputs iterable give output a list of tuples iterable
cities = ['mumbai','new york','paris']
countries = ['India','USA','France']
z = zip(cities,countries)
print(z)
for a in z:
  print(a)

# single argument zip 
z = zip(a)
for a in z :
  print(a)

# combine dictionary keys and values
d = {'name': 'Felix', 'age': 27, 'grade': 'A'}
a = d.keys()
b = d.values()
z = zip(a,b)
print(list(z))

# unzipping
a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
fruits,values = zip(*a)
print("Fruits:", fruits)
print("values:", values)