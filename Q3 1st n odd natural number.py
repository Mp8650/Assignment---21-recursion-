'''a recursive python function to print first
 N  odd natural numbers.'''
def printN(n):
    if n>=1:   
        printN(n-1)
        print(2*n-1)
printN(int(input("enter a number")))

    
  