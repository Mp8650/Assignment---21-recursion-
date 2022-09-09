'''a recursive python function to print 
cube of first N natural numbers '''
def printN(n):
    if n>=1:
        
        printN(n-1)
        print(n**3)
printN(int(input("enter a number")))

    
  