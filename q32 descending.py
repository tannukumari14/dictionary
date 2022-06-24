# a={"tanu":56,"pinky":30,"sarita":90,"sheetal":100,"simran":52}
# sort={k:v for k,v in sorted(a.items(),key=lambda v:v[1],reverse=True)}
# print(a)
# print(sort)

# a={"tanu":56,"pinky":30,"sarita":90,"sheetal":100,"simran":52}
# sort={k:v for k,v in sorted(a.items(),key=lambda v:v[1])}
# print(a)
# print(sort)

dict = {'a':70, 'b':8, 'c':68,'d':30, 'e':0, 'f':10}
for i in dict:
    for j in dict:
        if dict[i]>dict[j]:
            dict[i],dict[j]=dict[j],dict[i]
print(dict)