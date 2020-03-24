def createstar():
    n = int(input("enter the no of column->"))
    for i in range(n):
        print("* " * (i+1))
    for i in range(n-1):
        print("* " * (n-i-1))
        
createstar()