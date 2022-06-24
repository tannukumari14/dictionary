dic={"ishu":10,"tanu":90,"simran":79,"nisha":9,"kareena":45}
for i in dic:
    for j in dic:
        if dic[i]<dic[j]:
            dic[i],dic[j]=dic[j],dic[i]
print(dic)
