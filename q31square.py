a=int(input("enter the number"))
i=0
b={}
while i<=a:
    c=i,i*i
    b.update({c})
    i=i+1
print(b)