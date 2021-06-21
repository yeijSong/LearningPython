'''
menu=['orange','strawberry','peach','mango','grape','soldout']
price=[1000,2500,1500,2000,2000]
print('*****홍익대학교 과일 판매머신v03*****')

for n in range(0,5):
	print(n+1,'번',menu[n],':',price[n],'원')
print('6.soldout')
print('==============================')

while True:
	n=int(input('구매번호를 입력하세요(1-6)'))
	if n==1:
		print(menu[n-1],'는',price[n-1],'원 입니다')
	elif n==2:
		print(menu[n-1],'는',price[n-1],'원 입니다')
	elif n==3:
		print(menu[n-1],'는',price[n-1],'원 입니다')
	elif n==4:
		print(menu[n-1],'는',price[n-1],'원 입니다')
	elif n==5:
		print(menu[n-1],'는',price[n-1],'원 입니다')
	elif n==6:
		break
'''
menu=['orange','strawberry','peach','mango','grape','soldout']
price=[1000,2500,1500,2000,2000]
print('*****홍익대학교 과일 판매머신v03*****')

for n in range(0,5):
	print(n+1,'번',menu[n],':',price[n],'원')
print('6.soldout')
print('==============================')

while True:
	n=int(input('상품 번호를 입력해주세요(1~6)'))

	if n in range(1,6):
		print(menu[n-1],'는',price[n-1],'원 입니다.')
	else:
		print('soldout')
		break