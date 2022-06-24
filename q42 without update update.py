# a={"name":"khushubhu katyura"}
# a["name"]="tanu kumari"
# print(a)

# a=["name","class"]
# b=[1,2]
# i=0
# c={}
# while i<len(a):
#     c.update({a[i]:b[i]})
#     i=i+1
# print(c)

# list=[]
# a={"name":"tanu","friends":"sneha"}
# list.append(a["friends"])
# a["friends"]="khushboo"
# list.append(a["friends"])
# a.update({"friends":list})
# print(a)


a=["a","b","c","d"]
b=["e","f","g","h"]
i=0
c={}
while i<len(a):
    h=a[i]+b[-1]
    c.update({i:h})
    i=i+1
print(c)


