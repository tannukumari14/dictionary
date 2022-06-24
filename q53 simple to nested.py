a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
i=0
f={}
while i<len(c):
    f.update({a[i]:{b[i]:c[i]}})
    i+=1
print(f) 

