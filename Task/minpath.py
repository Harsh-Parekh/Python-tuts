"""
list=[
        [2],
       [4,5],
      [8,5,3],
     [7,8,9,1]
]
so min path to traverse is 2+4+3+1=10
"""








mainls=[]
numls=int(input("Enter no list :"))
for i in range(1,numls+1):
    col = []
    print("Enter data in list %d"%i)
    for j in range(i):
        col.append(int(input("Enter data :")))
    mainls.append(col)

print(mainls)
total=0

for j in range(len(mainls)):
    a=min(mainls[j])
    total=total+a
print("Min Path to traversle :",total)


