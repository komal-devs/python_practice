#deque as generalisation of stack
from collections import deque
class Stack :
  def __init__(self):
    self.container = deque()
  def push(self,value):
    self.container.append(value)
  def pop(self):
    return self.container.pop()
  def peek(self):
    return self.container[-1]
  def size(self):
    return len(self.container)
  def is_empty(self):
    return len(self.container) == 0

# function that reverses a string
def reverse_string(s):
  stack = Stack()
  for ch in s :
    stack.push(ch)
  rstr = ""
  while stack.size() != 0 :
    rstr += stack.pop()
  return rstr

# function that checks parenthesis are balanced or not
def is_balanced(s):
  stack = Stack()
  pairs = ['(',')','{','}',']','[']
  for ch in s :
    if ch in '({[':
      stack.push(ch)
      if ch in ')}]':
        if stack.is_empty():
          return False
    else:
      char = stack.peek()
      if (ch == ')' and char == '(') or (ch == ']' and char == '[') or (ch == '}'and char == '{'):
        return True
  return len(stack == 0)


    
if __name__ == '__main__' :
  print(reverse_string("komal is an ambitious girl"))
s = Stack()
s.push("https://www.cnn.com/")
s.push("https://www.cnn.com/world")
s.push("https://www.cnn.com/india")
s.push("https://www.cnn.com/china")
print(s)
print(s.pop())
print(s.pop())
print(s.peek())
print(s.size())
print(s.is_empty())
str= '((())){{}}[[]]'
print("stack is balanced ---- ")
print(is_balanced(str))
  

# stack data structure as list implementation
s = []
s.append("a")
s.append("b")
s.append("c")
s.append("d")
print(s)
s.pop()
print(s[-1])
print(s.pop())
print(s.pop())
print(s.pop())





