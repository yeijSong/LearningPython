#< 딕서녀리 관련 함수들 >

#Key 리스드 만들기(Keys)

a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())
print('')

'''
dict_keys,dict_values,dic_items 등은 리스트로 변환하지 않더라도
기본적인 반복(iterate)구문(ex_for문)을 실행할 수 있다.
'''
for k in a.keys():
	print(k)

print('')

#dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
vList=list(a.keys())
print(vList)
