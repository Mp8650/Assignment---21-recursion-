'''a recursive python function to print square of first
 N natural numbers '''
def printN(n):
    if n>=1:
        
        printN(n-1)
        print(n*n)
printN(int(input("enter a number")))

    
  