
menu = ['1. 회원가입', '2. 로그인', '3. 회원목록', '9. 메뉴종료']
menuChk = ['1','2','3','9']

print('{0:=^56}'.format('메뉴선택'))
print('')
print(menu)
print('')
print('='*60)
print('')


while True:
	a=input('{0:>10}'.format('메뉴의 번호를 선택해주세요'))

	if a=='':
		print('{0:>20}'.format('다시 입력해주세요'))
		continue
	elif a!='':
		a=int(a)

	if a in range(1,4):
		print('{0:>20}'.format(menu[a-1]),'Algorithm Chk')

	elif a==9:
		print('{0:>20}'.format(menu[3]))
		break

	else:
		print('메뉴의 번호를 다시 확인해주세요')


