def Fibonacci_sequence(n):

    if n <= 0:
        print("Error!!! input a positive integer!")
        
    elif n == 1:
        print(0)
        return
    
    a, b  = 0, 1
    for i in range(n):
        print(a, end= " ")
        a, b = b, a + b

n = int(input("Enter a positive integer: "))

Fibonacci_sequence(n)