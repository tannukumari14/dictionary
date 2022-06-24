# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# b=[]
# num={}
# for a,c in dic.items():
#     if c not in b:
#         num[a]=c
# print((num))

# test_dict = { 'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
# temp = []
# res = dict()
# for key, val in test_dict.items():
#     if val not in temp:
#         temp.append(val)
#         res[key] = val
# print("The dictionary after values removal : " + str(res)) 


a=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, 
{"six":"9"},{"seven":"7"}]
i=0
b={}
c=[]
while i<len(a):
  b.update (a[i])
  i=i+1
for i in b.values():
  if i not in c:
    c.append(i)
print(c)