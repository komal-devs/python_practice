basket = {'orange','apple','banana','litchi','mango'}
print(type(basket))
print(basket)
a = set() # way of creating empty set
print(type(a))
a.add(1)
a.add(2)
a.add(3)

print(a)
a = {} # will create empty dictionary
print(type(a))
# set is unordered collection of unique elments
# print(basket[0]) 
numbers = {1,2,3,4,5,3,2,5}
print(numbers)
# frozenset - create set that cannot be changed later
unique_numbers = frozenset(numbers)
print(unique_numbers)
# unique_numbers.add(6) -- throw an error

x = { "s","b","t"}
y = {"s","a"}
# set union using | operator
print(x|y)
# set intersection using & operator
print(x&y)
print(x-y)
# check subset using < operator
print(y< x)
y = {"s"}
print(y< x)
