a = 2
b = 3

# a = a+b
# b = a-b
# a = a-b
"""b = (a+b)-b，这就是说a+b=5再减去b的值3就剩下2，所以b就是2
   a = (a+b)-b，这时5减去现在的b值是2，所以a=3，不知对否？"""

c = b
b = a
a = c
"""让c水桶装了b水桶的水，然后把a水桶的水倒入b水桶，这时a就是b了；
   再让c水桶的水倒入a水桶，这时b就是a了"""
# 
# a,b = (b,a)
# a,b = b,a

print(a)
print(b)
