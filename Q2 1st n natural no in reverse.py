'''a recursive python function to print first
 N natural numbers in reverse order.'''
def printN(n):
    if n>0:
        print(n)
        printN(n-1)
printN(int(input("enter a number")))

    
  