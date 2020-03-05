list1, list2 = [123, 'xyz', 'Nimesh'], [456, 'abc']
print("First list length : ", len(list1))
print("Second list length : ", len(list2))

# Output
# First list length :  3
# Second list length :  2

aTuple = (123, 'xyz', 'Nimesh', 'abc')
aList = list(aTuple)
print("List elements : ", aList)

# Output 
# List elements :  [123, 'xyz', 'Nimesh', 'abc']


list1 = [123, 45, 3, 2]
print(max(list1))
print(min(list1))

# Output 123
# 2


aList = [123, 'xyz', 'Nimesh', 'abc']
aList.append( 2009 )
print("Updated List : ", aList)

# Output 
# Updated List :  [123, 'xyz', 'Nimesh', 'abc', 2009]

aList = [123, 'xyz', 'Nimesh', 'abc', 123]

print("Count for 123 : ", aList.count(123))

# Output 
# Count for 123 :  2


aList = [123, 'xyz', 'Harshal', 'abc', 123]
bList = [2009, 'Nimesh']
aList.extend(bList)
print("Extended List : ", aList)

# Output 
# Extended List :  [123, 'xyz', 'Harshal', 'abc', 123, 2009, 'Nimesh']


aList = [123, 'xyz', 'Nimesh', 'abc']
print("Index for xyz : ", aList.index( 'Nimesh' ))

# Output 
# 2

aList = [123, 'xyz', 'Nimesh', 'abc']
aList.insert( 3, 2009)
print("Final List : ", aList)

# Output 
# Final List : [123, 'xyz', 'Nimesh', 2009, 'abc']

### Pop's out using index(int argument)
aList = [123, 'xyz', 'Nimesh', 'abc']

print("A List : ", aList.pop())
print(aList)
# A List :  abc
# [123, 'xyz', 'Nimesh']

print("B List : ", aList.pop(2))
print(aList)
# B List :  Nimesh
# [123, 'xyz']

aList = [123, 'xyz', 'Nimesh', 'abc', 'xyz']

aList.remove('xyz')
print("List : ", aList)

# Output
# List :  [123, 'Nimesh', 'abc', 'xyz']

aList = [123, 'xyz', 'Nimesh', 'abc', 'xyz']
aList.reverse()
print("List : ", aList)

# Output
# List :  ['xyz', 'abc', 'Nimesh', 'xyz', 123]

aList = [123,47.5,123456789.66666666]
aList.sort()
print("List : ", aList)

# Output
#  [47.5, 123, 123456789.66666666]
