dic={'name':'pey','phone':'0119993323','birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

print('\n')

#딕셔너리에서 key값은 중복될 수 없다.
#따라서 key값이 중복될 경우 
#언어에 따라 에러가 나거나 뒷 부분의 정보로 덮어쓰기되거나 아예 무시되기도 한다
a={1:'a',1:'b'}
print(a)
