str="this is string example"

print("Full string reverse")
print(str[-1:-23:-1])
#Full string reverse
#elpmaxe gnirts si siht

print("only word reverse")
string=str.split()
s1=string[0][::-1],string[1][::-1],string[2][::-1],string[3][::-1]
s=" "
seq = (s1)
print(s.join(seq))
#only word reverse
#siht si gnirts elpmaxe

print("string*string*string")
sub=str.split(s)
s1="*"
print(s1.join(sub))
#string*string*string
#this*is*string*example

print("replace")
print(str.replace(" is"," was"))
#replace
#this was string example

print("only two char swap")
sub1=string[0][0:2][::-1]+string[0][2:4][::-1]+" "+string[1][0:2][::-1]+" "+string[2][0:2][::-1]+string[2][2:4][::-1]+string[2][4:6][::-1]+string[2][6:8][::-1]+" "+string[3][0:2][::-1]+string[3][2:4][::-1]+string[3][4:6][::-1]+string[3][-1]
print(sub1)
#only two char swap
#htsi si tsirgn xemalpe
