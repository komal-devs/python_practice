def add_item(x):
  x.append(200)
  print("Inside function ", x)
x= [2,4,6,8]
add_item(x)
print("outside function ",x)

# mutable objects are passed by references
# so changes get reflected