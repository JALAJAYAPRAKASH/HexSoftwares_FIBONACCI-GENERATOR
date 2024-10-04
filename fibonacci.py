def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

n = int(input("Enter the number of terms: "))
for i in range(1,n+1):
    print(fibonacci(n))