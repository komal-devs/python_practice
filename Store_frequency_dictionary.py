# program to store frequency in dictionary
num = [1,2,3,4,111,1,1,2 ,4]
dic = dict()
for i in range(0,len(num)):   # O(N)
  if num[i] in dic :
    dic[num[i]] += 1     # O(1)
  else :
    dic[num[i]] = 1
print(dic)
# time complexity - O(N)    ... in dic on average case is taken
# ... worst case - one in a while
# space complexity - O(n)

# another method
num = [1,2,3,4,111,1,1,2 ,4]
dic = dict()
for i in range(0,len(num)):
  dic[num[i]] = dic.get(num[i],0) + 1
print(dic)
