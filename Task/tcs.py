def p_or_not(var):
    if var==1:
        return False
    sqrt=int(var**0.5)
    flag=0
    for i in range(2,sqrt+1):
        if var%i==0:
            flag=1
            break
    if flag==0:
        return True

no1,no2=map(int,input("Enter no 1 and no 2 :").split())

primes_collection=[]
for i in range(no1,no2+1):
    chk=p_or_not(i)
    if chk==1:
        primes_collection.append(i)
        pass
print(primes_collection)
ls_combi=[]
for i in range(len(primes_collection)):
    for j in range(len(primes_collection)):
        if i==j:
            continue
        else:
            ls_combi.append(int(str(primes_collection[i])+str(primes_collection[j])))
l=set(ls_combi)
ls_combi=list(l)
print(ls_combi)

new_primes=[]
for i in ls_combi:
    a=p_or_not(i)
    if a==True:
        new_primes.append(i)
print(new_primes)

maxi=max(new_primes)
mini=min(new_primes)

fib=[0]*(len(new_primes)+1)
fib[0]=mini
fib[1]=maxi
fib[2]=mini+maxi
for i in range(3,len(new_primes)+1):
    fib[i]=fib[i-1]+fib[i-2]
print(fib)
print(fib[len(new_primes)-1])