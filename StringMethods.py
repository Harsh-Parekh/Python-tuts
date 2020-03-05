# String all methods.
a = "hello"

print(len(a))
# Output : 5

print(a.capitalize())
# Output : Hello

str = "this is string example"
sub = "i"
print("count:", str.count(sub, 4, 21))
# Output : count: 2

str1 = "this is string example"
str2 = "exam"
print(str1.find(str2))
# Output : 15

s = "-"
seq = ("a", "b", "c")  
print(s.join(seq))
# Output : a-b-c

str = "this is string example"
print(str.split(' '))

# Output : ls=['this', 'is', 'string','example']

str = "THIS IS STRING EXAMPLE"
print(str.isupper())
# Output : True

str = "THIS is string example"
print(str.isupper())
# False

str = "hello"
print(str.islower())
# Output : True

# The method lower() returns a copy of the string in which all case-based characters have been lowercased.
str = "THIS IS STRING EXAMPLE"
print(str.lower())
# Output : this is string example

str = "hello"
print(str.upper())
# Output:HELLO

str = "this is string example"
print(str.replace("is", "was"))
# Output : thwas was string example

b = "5"
print(b.isdigit())
# Output : True