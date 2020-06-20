ls=[]
flag=0
lent=int(input("Enter lenght of array :"))
for i in range(0,lent):
    val=int(input("Enter number :"))
    ls.append(val)
ls.sort()
for i in range(0,len(ls)):
    if i!=ls[i]:
        print("Smallest +ve int is : %d"%i)
        flag=flag+1
        break
if(flag==0):
    print("Smallest +ve int is :",len(ls))