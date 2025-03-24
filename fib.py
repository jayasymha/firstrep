# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    fib_series = [0, 1]  # Starting values for Fibonacci series
    
    # Generate the Fibonacci sequence up to the nth term
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series

# Input: number of terms
n = int(input("Enter the number of terms in Fibonacci series: "))

# Generate and print the Fibonacci series
fib_series = fibonacci(n)
print(f"The first {n} terms of the Fibonacci series are:")
print(fib_series)
