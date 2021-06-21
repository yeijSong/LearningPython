# 값 변환

#방법1(대부분의 언어에서 통용되는)
vI01=20
vI02=30

print('교환 전 값:',vI01,vI02)

temp=vI01
vI01=vI02
vI02=temp

print('교환 후 값:',vI01,vI02)

#방법2(파이썬에서 가능한)

a=3
b=5

print('교환 전 값:',a,b)
a,b=b,a
print('교환 후 값:',a,b)
