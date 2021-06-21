#Key로 Value얻기(get)
a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.get('name'))
print('')

'''
get(x)함수는 x라는 key에 대응되는 value를 돌려준다.
a['yes']는 key오류를 발생시키고,
a.get('no')는 None을 돌려준다는 차이가 있다.
'''
print(a.get('no'))
print(a['yes'])