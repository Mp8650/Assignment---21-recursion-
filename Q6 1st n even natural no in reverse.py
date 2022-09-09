'''a recursive python function to print first
 N  even natural numbers in reverse.'''
def printN(n):
    if n>=1:
        print(2*n)
        printN(n-1)
        
printN(int(input("enter a number")))

    
  