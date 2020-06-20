"""
Stack using list
bascis of stack :-
1) Lifo(last in first out)
2) opertaion's :
    1) push - insert element
    2) pop  - remove element
    3) peep - check top of stack
3) usage in Website(control flow),memory,etc
"""
class Stack:
    ls=[]
    def __init__(self,cap):
        self.cap=cap

    def push(self,ele):
        if len(self.ls)<self.cap:
            self.ls.append(ele)
        else:
            print("Stack over flow...")
        print("stack is :",self.ls)

    def pop(self):
        if len(self.ls)==0:
            print("Stack under flow...")
        else:
            a=self.ls.pop()
            print("pop element is :",a)
        print("Stack is :",self.ls)

    def peep(self):
        if len(self.ls)==0:
            print("Stack empty...")
        else:
            print("Top element of stack is :",self.ls[len(self.ls)-1])

S=Stack(int(input("Enter capacity :")))
while True:
    print()
    print("1 push ")
    print("2 pop ")
    print("3 peep ")
    print('4 exit ')
    a=int(input("Enter choice :"))
    if a==1:
        print()
        S.push(int(input("Enter element :")))

    elif a==2:
        S.pop()

    elif a==3:
        S.peep()

    elif a==4:
        break
    else:
        print("Wrong choice...")