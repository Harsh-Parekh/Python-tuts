str=""
num=int(input("Enter number :"))
val=num
while num>0:
    if num%2==0:
        str=str+'0'
    else:
        str=str+'1'
    num=(num//2)

chk=len(str)
if chk%2!=0:
    str=str+'0'

bin=str[::-1]
print("binary of %d :"%val,bin)

first=bin[0:4]
sec=bin[4:8]

swapdt=sec+first
print("swap value is :",swapdt)

print(int(swapdt,2))
