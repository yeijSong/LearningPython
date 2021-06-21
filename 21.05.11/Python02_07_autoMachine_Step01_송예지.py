'''
홍익대학교 과일 판매머신 V01
1.orange:1000원
2.strawberry=2500원
3.peach=1500원
4.mango=2000원
5.grape=2000원
6.판매종료

구매번호를 입력하세요

조건1 해당번호를 입력 -> orange 1000원입니다
조건2 
'''
'''
print(*****홍익대학교 과일 판매머신 V01*****)
print("1=Orange=1000원")
print("2=Strawberry=2500원")
print("3=Peach=1500원")
print("4=Mango=2000원")
print("5=Grape=2000원")
print("6=판매종료")

no=int(input("구매 번호를 입력하세요"))
if no=1:
	print("Orange 1000원입니다")
elif no=2:
	print("Strawberry 2500원입니다")
elif no=3:
	print("Peach 1500원입니다")
elif no=4:
	print("Mango 2000원입니다")
elif no=5:
	print("Grape 2000원입니다")

while no!=6:


result=int(input())
print(result)
'''

###
print("*****홍익대학교 과일 판매머신 V01*****")
print("1.Orange     : 1000원")
print("2.Strawberry : 2500원")
print("3.Peach      : 1500원")
print("4.Mango      : 2000원")
print("5.Grape      : 2000원")
print("6.판 매 종 료")



while True:
	no=int(input("구매 번호를 입력하세요"))
	if no==1:
		print("Orange 1000원입니다")
	elif no==2:
		print("Strawberry 2500원입니다")
	elif no==3:
		print("Peach 1500원입니다")
	elif no==4:
		print("Mango 2000원입니다")
	elif no==5:
		print("Grape 2000원입니다")
	elif no==6:
		print("판매종료")
		break