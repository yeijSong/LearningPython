

while True:
	
	n=int(input('10이상의 숫자를 입력해주세요:'))

	if n==0:
		print('종료!')
		break
	elif n<10:
		print('숫자를 다시 확인해주세요')
	elif n>=10:
		print('===<<%d번 반복합니다,>>=='%n)
		FL=[]
		All=[]
		for i in range(1,n+1):
			
			if i%3==0:
				FL.append('Apple')
			if i%4==0:
				FL.append('Melon')
				
			if i%5==0:
				FL.append('Grape')
				
			if i%8==0:
				FL.append('StrawBerry')
			
			All=All+FL
			
			
			if len(FL)==0:
				print('%d.'%i)
			else:
				print('%d.'%i,FL)
			FL=[]
		print("==== << Fruit Count List >> ====")
		print("     Apple:%10d회"%All.count('Apple'))
		print("     Melon:%10d회"%All.count('Melon'))
		print("     Grape:%10d회"%All.count('Grape'))
		print("     StrawBerry:%5d회"%All.count('StrawBerry'))
		print("-"*32)
