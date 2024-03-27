def fibonacci(n):
    fibonacci = [0,1]
    for i in range(0,n):
        temp = fibonacci[i] + fibonacci[i+1]
        fibonacci.append(temp)
    return fibonacci


output = fibonacci(10)
print(output)