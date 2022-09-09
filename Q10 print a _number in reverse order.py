'''  a recursive python function to print a 
number in reverse order. '''

def printN(n):
    rev=0
    if n>0:
        rem=n%10
        rev=rev*10+rem
        print(rev,end='')
        printN(n//10)
printN(int(input("Enter a number")))
    