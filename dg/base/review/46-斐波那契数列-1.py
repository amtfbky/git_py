def fibNum(n):
    a, b = 0, 1
    for i in range(n):
        b, a = a+b, b
    return b

num = int(input(">>:"))

if num == 1:
    print(0)
elif num == 2:
    print(1)
else:
    print(fibNum(num-2))
