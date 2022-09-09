'''a recursive python function to print first
 N  even natural numbers.'''
def printN(n):
    if n>=1:
        
        printN(n-1)
        print(2*n)
printN(int(input("enter a number")))

    
  