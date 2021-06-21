'''
딕셔너리 안에 찾으려는 Key값이 없을 경우
미리 정해둔 디폴트 값을 대신 가져오게 하고 싶을 때에는
get(x, '디폴트 값')을 사용하면 편리하다.

아래 예시를 보면 딕셔너리 a에 'foo'에 해당하는 값이 없기 때문에
디폴트 값인 'bar'를 돌려준다.
'''

a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('foo','bar'))
print('\n')

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in a)
print('email' in a)