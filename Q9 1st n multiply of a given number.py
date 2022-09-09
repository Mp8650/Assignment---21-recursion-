'''a recursive python function to print 
first N multiply of a given number '''
def printN(n,num):
    if n>=1:
        
        printN(n-1,num)
        print(n*num)
printN(int(input("Enter number of multiple")),int(input("Enter number to multiply")))
