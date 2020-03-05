ls=[1,1,"Asit","Harshal",'N',45.5,45.5]

print(ls)
#[1, 1, 'Asit', 'Harshal', 'N', 45.5, 45.5]

print(ls[0])
#1

print(ls[0:2])
#[1, 1]

print(ls[0:])
#[1, 1, 'Asit', 'Harshal', 'N', 45.5, 45.5]

ls[5]=66

print(ls)
#[1, 1, 'Asit', 'Harshal', 'N', 66, 45.5]

ls.append("Harsh")
print(ls)
#[1, 1, 'Asit', 'Harshal', 'N', 66, 45.5, 'Harsh']

print(type(ls))
#<class 'list'>