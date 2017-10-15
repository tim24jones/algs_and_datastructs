def factorial(n):
    if n<=1:
        fact=1
    elif n>1:
        fact=n*factorial(n-1)
    return fact
print(factorial(5))