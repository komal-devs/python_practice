first = [1,2,3]
second = first.copy()
second.append(200)
print(id(first))
print(id(second))

print(first is second)

# another method using copy module
import copy
first = [2,3,4,5]
second = copy.copy(first)
print(id(first))
print(id(second))
second.append(8)
print(first)
print(second)


original = [99,34,67,[1,2,3],90]
shallow = copy.copy(original)
shallow[3][1] = 0  # element of mutable element changing also reflects in original 
# to avoid this deep copy is used
shallow[4] = 70
print(original)
print(shallow)