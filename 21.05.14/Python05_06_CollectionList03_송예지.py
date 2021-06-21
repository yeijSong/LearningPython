print('*리스트의 슬라이싱*')

a=[1,2,3,4,5]
print(a[0:2])
print(a[:2])
print(a[2:])
print('-'*15)

print('*중첩된 리스트에서 슬라이싱하기*')

b=[1,2,3,['a','b','c'],4]
print(b[2:5])
print(b[3][:2])
print('-'*15)