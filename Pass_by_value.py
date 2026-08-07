def increment(x):
  x = x+ 1
  print("inside function",x)
num = 10
increment(num)
print(f"outside function {num}")

# copy of immutable objects are passed so 
# changes doesnt reflect