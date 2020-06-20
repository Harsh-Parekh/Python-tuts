
class Queue:

    que=[]
    def __init__(self,limit_of_que):
        self.limit_of_que=limit_of_que

    def enque(self,ele):
        if len(self.que)!=self.limit_of_que:
            self.que.insert(0,ele)
        else:
            print("Limit execed...!")
        print("Queue is :",self.que)

    def deque(self):
        if len(self.que)==0:
            print("Queue empty...!")
        else:
            a=self.que.pop()
            print("Element remove is :",a)
        print("Queue is :",self.que)

    def peek(self):
        if len(self.que)==0:
            print("Ohhh queue is empty...")
        else:
            print("Element at front is :",self.que[-1])
            print("Element at end is :",self.que[0])

    def isempty(self):
        if len(self.que)==0:
            return True
        else:
            return False


limit=int(input("Enter limit of queue :"))
q=Queue(limit)
while True:
    print()
    print("1 add element ")
    print("2 remove element ")
    print("3 peek ")
    print("4 isempty ")
    print('5 exit ')
    a = int(input("Enter choice :"))
    if a==1:
        q.enque(int(input("Enter element :")))
    elif a==2:
        q.deque()
    elif a==3:
        q.peek()
    elif a==4:
        ans=q.isempty()
        print(ans)
    elif a==5:
        break
    else:
        print("Wrong choice...!")
