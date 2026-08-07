import copy
original = [99,34,67,[1,2,3,4],90]
shallow = copy.deepcopy(original)
shallow[3][1] = 0  
shallow[4] = 70
print(id(original))
print(id(shallow))
print(original)
print(shallow)