original = [1,2,3]
print(id(original))
copy = original
print(id(copy))
copy.append(100)
print(copy)
print(original)
print(original is copy)  # return True if both have same memory address
print(original==copy)  # return true if the contents of both list are same



# creating list without assignment operator
a = [1,2,3]
b = [1,2,3]
print(a is b)
print(a == b)