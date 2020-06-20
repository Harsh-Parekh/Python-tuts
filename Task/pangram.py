str=input("Enter string :")
alpha="abcdefghijklmnopqrstuvwxyz"
for i in alpha:
    if i not in str.lower():
        print("FAlSE")
        break
else:
    print("True")