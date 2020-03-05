tupl=(1,1,"Asit","Harshal",'N',45.5,45.5)

print(tupl)
#[1, 1, 'Asit', 'Harshal', 'N', 45.5, 45.5]

print(tupl[0])
#1

print(tupl[0:2])
#[1, 1]

print(tupl[0:])
#[1, 1, 'Asit', 'Harshal', 'N', 45.5, 45.5]

#tupl[5]=66
#'tuple' object does not support item assignment

print(tupl)
#[1, 1, 'Asit', 'Harshal', 'N', 66, 45.5]

print(type(tupl))
#<class 'list'>