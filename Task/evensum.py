no=int(input("enter no 1 to "))
num=1
li=[]
for i in range(0,no):
    li.append(num)
    num=num+1
count=0
for i in range (0,no):
    for j in range (i+1,no):
        for k in range (j+1,no):
            if (li[i]+li[j])%2==0:
                if li[k]%2==0:
                    count=count+1
                    print(li[i],li[j],li[k])
            else:
                if li[k]%2!=0:
                    count=count+1
                    print(li[i],li[j],li[k])

print("no of ways for selecting three num which sum is even: ",count)

