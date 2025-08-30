def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact

num = 5
print("factorial of", num, "is", factorial(num))
