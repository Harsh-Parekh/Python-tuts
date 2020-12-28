
class Stack:

    def __init__(self):
        self.ls = []
        pass

    def push(self, data):
        self.ls.append(data)
        pass

    def pop(self):
        poped_ele = self.ls.pop()
        return poped_ele

    def top(self):
        if len(self.ls)>0:
            return self.ls[-1]
        else:
            return -1
    def isempty(self):
        if len(self.ls) == 0:
            return "YES"
        else:
            return "NO"

    def ret_stack(self):
        return self.ls


obj_stack = Stack()

while True:
    print("1. Add data")
    print("2. Remove data")
    print("3. isempty?")
    print("4. current stack")
    print("5. top")
    print("6. Exit")
    print("Enter choice: ")
    action = int(input())
    if action == 1:
        obj_stack.push(int(input("Enter data :")))
        print("data pushed")
    elif action == 2:
        ret_statement = obj_stack.pop()
        print(ret_statement)
    elif action == 3:
        ret_val = obj_stack.isempty()
        print(ret_val)
    elif action == 4:
        ret_statement = obj_stack.ret_stack()
        print(ret_statement)
    elif action == 5:
        ret_statement = obj_stack.top()
        print(ret_statement)
    elif action == 6:
        break
