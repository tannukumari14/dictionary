# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# k={}
# i=0
# while i<len(d1):
#     if d1 in d2:
#         k.update({d1[i]:d2[i]})
#     i=i+1
# print(k)

# char_list =["w3resource"]
# i=0
# a=[]
# while i<len(char_list):
#     j=0
#     b=[]
#     count=0
#     while j<len(char_list):
#         if char_list[i] in char_list:
#             if char_list[i]==char_list[j]:
#                 count=count+1
#         j=j+1
#     b.append(char_list[i])
#     b.append(count)
#     if b not in a:
#         a.append(b)
#     i=i+1
# print(a)

# a={0:10,1:20}
# a[2]=30
# print(a)

# dic1={1:10,2:20}
# dic2={3:30,4:40}
# dic3={5:50,6:60}
# b={}
# i=0
# while i<len(dic1):
#     b.update(dic1)
#     b.update(dic2)
#     b.update(dic3)
#     i=i+1
# print(b)

# dic1={"tanu":"airhostress","husna":"independenet","sarita":"fashion desinger"}
# dic2={"khushboo":"chai wali","kiran":"earn money"}
# i=0
# b={}
# while i<len(dic1):
#     b.update(dic1)
#     b.update(dic2)
#     i=i+1
# print(b)

# a={"tanu":12,"sarita":17,"pinky":17,"husna":17}
# i=0
# while i<len(a):
#     i=i+1
# print(a)

# a={1:2,3:4,5:6}
# Values=a.values()
# total=sum(Values)
# print(total)

# a={1:2,3:4,5:6,7:8}
# sum=0
# for i in a:
#     sum=sum+a[i]
# print(sum)

# a={1:2,3:4,5:6}
# answer = 1
# for i in a:
#     answer = answer*a[i]
# print(answer)

# a={1:"tanu","husna":3,"khushboo":8}
# b=a.values()
# print(b)

# a={"tanu":1,"unat":2,"leethas":3}
# a.sort()
# print(a)

# student={"id1":{"name":["sara"],"class":["v"],
# "subject_intergration":["english,maths,science"]
# },"id2":{"name":["david"],"class":["v"],"subject_intergration":["english,maths,science"]},
# "id3":{"name":["sara"],"class":["v"],"subject_intergration":["english,maths,science"]
# },"id4":{"name":["surya"],"class":["v"],"subject_intergration":["english,maths,science"]},}

from binascii import b2a_hex
from operator import iadd
from re import L


# a= [{"V":"S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII":"S005"},
# {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in a:
#     for j in i.values():
#         b.append(j)
# i=0
# c=[]
# while i<len(b):
#     if b[i] not in c:
#         c.append(b[i])
#     i=i+1
# print(c)        

# a=["tanu","kumari"]
# b=[1,2]
# i=0
# c={}
# while i<len(a):
#     c.update({a[i]:b[i]})
#     i=i+1
# print(c)

# a={"a":100,"b":200,"c":300}
# b={"a":300,"b":200,"d":400}
# for i in a:
#     if i in b:
#         b[i]=a[i]+b[i]
#     else:
#         b[i]=a[i]
# print(b) 

# a={"name":"tanu","class":12,"age":16}
# b=a.values()
# c=a.keys()
# d=[]
# e=[]
# d.append(b)
# print(d)
# e.append(c)
# print(e)

# a=["tanu","ankita","anjali ","simran"]
# i=0
# count=0
# while i<len(a):
#     count=count+i
#     i=i+1
#     print(count)

# a={"a 001":["maths","science"],"s 002":["mats","sience"]}
# b=a["a 001"]="a001"
# print(b)



# a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# max=1
# for i in a:
#     if a[i]>max:
#         max=a[i]
#         s=i
# print(max)
# max1=1
# for i in a:
#     if a[i]>max1:
#         if max!=a[i]:
#             max1=a[i]
#             s=i
# print(max1)
# max2=1
# for i in a:
#     if a[i]>max2:
#         if max!=a[i] and max1!=a[i]:
#             max2=a[i]
#             s=i
# print(max2)


