s={'A',"A",99,96.5}

print(s)
#{96.5, 99, 'A'}

print(type(s))
#<class 'set'>

#print(s[2])
#'set' object does not support indexing

#s[0]="ASIT"
#'set' object does not support item assignment

print(id(s))

s.add("ASIT")

print(s)

print(id(s))
