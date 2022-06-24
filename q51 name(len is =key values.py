a=["tanu","khushboo","pinky"]
i=0
dict={}
while i<len(a):
    dict.update({a[i]:len(a[i])})
    i=i+1
print(dict)
