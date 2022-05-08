'''def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
print(f(4))'''

'''def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
b=fib(5)
print(b) '''

def table(n,i):
    if i<=10:
        return(n*i)
    else:
        table(n,i+1)

print(table(4,10))
        
    


    
