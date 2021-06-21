'''
format 함수 안에는 인덱스값과 변수를 쓸 수 있다.
'''

a='my name is {}'.format('Hong')
b='{1}X{2}={0}'.format((11*2),11,2)
c='{p}X{q}={r}'.format(p=2,q=3,r=6)

print(a)
print(b)
print(c)