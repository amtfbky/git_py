# -*- coding:utf-8 -*-
b1 = reduce(lambda x,y:x+y, [1,2,3,4])
print(b1)

b2 = reduce(lambda x,y:x+y, [1,2,3,4], 5)
print(b2)

b3 = reduce(lambda x,y:x+y, ['aa','bb','cc'], 'dd')
print(b3)
