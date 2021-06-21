'''
[4일차 실습 예제01]

#소수 판별 프로그램 작성#

- 소수란?
	1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수.
	이를테면 2,3,5,7,11,13,17,19,23,29,31...등은 모두 소수.

- 조건
1. 사용자로부터 20이상의 수를 입력받는다.
2. n<20이면 '숫자확인하세요'
3. n>=20이면 소수 판별 출력

'''
'''

a=int(input('20이상의 숫자를 입력하세요:'))

if a>=20:
	b=0
	for i in range(2,a):
		if a%i==0:
			b=1
	if b==0:
		print('소수입니다')
	else:
		print('소수가 아닙니다')

else:
	print('숫자를 다시 확인하세요')

'''

'''
while True:
	a=int(input('20이상의 숫자를 입력하세요:'))

	if a>=20:
		b=0
		for i in range(2,a):
			if a%i==0:
				b=1
		if b==0:
			print('소수입니다')
		else:
			print('소수가 아닙니다')
	elif a==0:
		print('종료합니다')
		break
	else:
		print('숫자를 다시 확인하세요')

'''
'''
while True:
	a=int(input('20이상의 숫자를 입력하세요:'))

	if a>=20:
		for i in range(2,a+1):
			if a%i==0 and a!=i:
				print('소수가 아닙니다')
			elif a%i!=0 and a==i:
				print('소수입니다')
'''


while True:
	
	n=int(input("숫자를 입력하세요 :  [Exit : 0]"))
	
	if n==0:
		break
	
	elif n<20:
		print("20 이상의 수를 입력하세요")
	
	else:
		print("1.소수X")
		for j in range(2,n+1):
			a=0
			for i in range(2,j):
				if j % i==0:
					a=1
			if a==0:
				print("%d.소수O"%j)
			else:
				print("%d.소수X"%j)
			