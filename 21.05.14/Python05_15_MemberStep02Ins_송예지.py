itemList = ['ID', 'PWD', 'NAME', 'EMAIL', 'PHONE', 'ADDRESS']
menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']

print('{0:=^56}'.format('메뉴선택'))
print('')
for i in range(0,len(menu)):
	print(menu[i],end='\t')
print('')
print('='*60)
print('')

user_col=0
while True:
	a=input('{0:>10}'.format('메뉴의 번호를 선택해주세요'))

	if a=='':
		print('{0:>20}'.format('다시 입력해주세요'))
		continue
	elif a!='':
		a=int(a)

		if a==1:
			user_list=[]
			print(menu[0])
			for b in range(0,len(itemList)):
				result=str(input('%s : '%itemList[b]))
				user_list.append(result)
			user_col=user_col+1
			print(user_list)
			print('현재 회원수는 %d명입니다.'%user_col)


		if a in range(2,4):
			print('{0:>20}'.format(menu[a-1]),'Algorithm Chk')

		elif a==9:
			print('{0:>20}'.format(menu[3]))
			break

		else:
			print('메뉴의 번호를 다시 확인해주세요')


