list=[]
a={"name":"tanu","friends":"sneha"}
list.append(a["friends"])
a["friends"]="lateehs"
list.append(a["friends"])
a.update({"friends":list})
print(a)
