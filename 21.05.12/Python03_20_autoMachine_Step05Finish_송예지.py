'''
사용자가 번호 입력
1~5 이외의 숫자->번호를 다시 확인해주세요
코인을 투입하세요
투입된 금액은 __원 입니다.

선택한 과일
받은 금액

거스름돈
거스름돈은 __원 입니다.
금액 부족 확인
'''

menu=['orange','strawberry','peach','mango','grape']
price=[1000,2500,1500,2000,2000]
print('*****홍익대학교 과일 판매머신v05*****')

for n in range(0,5):
	print(n+1,'번',menu[n],':',price[n],'원')
print('6.soldout')
print('='*30)

while True:
	n=int(input('상품 번호를 입력해주세요(1~5)'))

	if n in range(1,6):
		print(menu[n-1],'는',price[n-1],'원 입니다.',end='\n\n')
	else:
		print('번호를 다시 확인해주세요',end='\n\n')

	p=int(input('코인을 투입하세요'))
	print('투입된 금액은 %d원입니다'%p,end='\n\n')
	print('='*30)
	print('선택한 과일은',menu[n-1],'이고, 받은 금액은%d원 입니다'%p,end='\n\n')
	print('='*30)

	if p>=price[n-1]:
            print('거스름돈은',p-(price[n-1]),'원입니다')
	else:
            print('금액부족')
	break