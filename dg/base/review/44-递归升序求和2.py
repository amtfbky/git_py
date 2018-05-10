def sum_number(num):
    if num > 1:
        return num+sum_number(num-1)
    else:
        return 1 

print(sum_number(100))
