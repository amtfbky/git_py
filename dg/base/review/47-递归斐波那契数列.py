def fibo(n):
    if n == 0 or n == 1:
        return n
    if n <= 3:
        return 1
    return fibo(n-1)+fibo(n-2)

n = int(input(">>:"))
print(fibo(n))
"""0 1 1 2 3 5 8 13 21 34 55...
   1 2 3 4 5 6 7 8  9  10 11..."""
