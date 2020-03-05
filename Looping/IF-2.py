x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    """print('Negative changed to zero')"""
    if x == 0:
        print('Zero')
elif x == 1:
    print('Single')
    if x == 0:
        print('Zero')
else:
    print('More')
