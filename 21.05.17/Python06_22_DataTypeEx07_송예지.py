#다른 주소를 가리키도록 만들 수는 없을까?

#방법1(슬라이싱)
a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)
print()

#방법2(copy, 외부 모듈을 가지고 옴)
from copy import copy
a=[1,2,3]
b=copy(a)
print(b)
print()
print(id(a))
print(id(b))


c=['보라돌이','뚜비','나나','뽀']
d=copy(c)
print(d)
print(id(c))
print(id(d))
c[3]='뽀뽀'
print(c)