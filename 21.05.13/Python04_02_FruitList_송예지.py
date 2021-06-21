'''
#알고리즘 확인#
- 조건 
1. 10이상의 숫자를 입력받는다.
2. 10미만의 숫자이면 숫자 확인하세요
3. 10이상이라면, 3으로 나눠 떨어진 수 : Apple
              4로             : Melon
			  5              : Grape
			  8               : StrawBerry 출력
4. 0이면 종료

'''

while True:
	n=int(input('10이상의 숫자를 입력해주세요:'))

	if n==0:
		print('종료!')
		break
	elif n<10:
		print('숫자를 다시 확인해주세요')
	elif n>=10:
		print('FruitList Algorithm Chk')