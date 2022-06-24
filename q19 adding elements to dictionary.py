# dic={"name":"tanu","age":"18"}
# dic["class"]=12
# dic["form"]="delhi"
# print(dic)

# dic={"name":"sneha","form":"delhi"}
# dic["who"]="sister"
# dic["year"]=2004
# print(dic)

# dic={1:10, 2:20}
# dic[3]=30
# dic[4]=40
# dic[5]=50
# dic[6]=60
# print(dic)

# dic1={1:10, 2:20}
# dic2={3:30,4:40}
# b={}
# i=0
# while i<len(dic1):
#     b.update(dic1)
#     b.update(dic2)
#     i=i+1
# print(b)

a=["one","two","three","four","five"]
b=[1,2,3,4,5]
k={}
i=0
while i<len(a):
    k.update({a[i]:b[i]})
    i=i+1
print(k)
