
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter number of terms: "))

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i))

def fibonacci_iterative(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[:n]

n_terms = int(input("Enter number of terms: "))
fib_series = fibonacci_iterative(n_terms)
print(f"\nIterative Fibonacci series (first {n_terms} terms): {fib_series}")