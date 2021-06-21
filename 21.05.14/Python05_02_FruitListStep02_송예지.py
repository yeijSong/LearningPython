'''
while True:
	a=0
	b=0
	c=0
	d=0
	num =int(input("10 이상의숫자를 입력하세요 :  [Exit : 0]"))
	
	if num==0:
		break
	
	elif num<10:
		print("10 이상의 수를 입력하세요")
	
	else:
		for j in range(1,num+1):
			col=[]
			if j%3==0:
				col.append("Apple")
				a=a+1
			if j%4==0:
				col.append("Melon")
				b=b+1
			if j%5==0:
				col.append("Grape")
				c=c+1
			if j%8==0:
				col.append("StrawBerry")
				d=d+1
			if len(col)==0:
				print("%d"%j)
			else:
				print("%d."%j,col)

		print("==== << Fruit Count List >> ====")
		print("Apple:%5d회"%a)
		print("Melon:%5d회"%b)
		print("Grape:%5d회"%c)
		print("StrawBerry:%5d회"%d)
		print("-"*30)
'''


A=0
M=0
G=0
S=0


while True:
	
	n=int(input('10이상의 숫자를 입력해주세요:'))

	if n==0:
		print('종료!')
		break
	elif n<10:
		print('숫자를 다시 확인해주세요')
	elif n>=10:
		print('===<<%d번 반복합니다,>>=='%n)
		
		for i in range(1,n+1):
			FL=[]
			if i%3==0:
				FL.append('Apple')
				A=A+1
			if i%4==0:
				FL.append('Melon')
				M=M+1
			if i%5==0:
				FL.append('Grape')
				G=G+1
			if i%8==0:
				FL.append('StrawBerry')
				S=S+1
			
			if len(FL)==0:
				print('%d.'%i)
			else:
				print('%d.'%i,FL)

		print('\n\n')
			

		print("==== << Fruit Count List >> ====")
		print("     Apple:%10d회"%A)
		print("     Melon:%10d회"%M)
		print("     Grape:%10d회"%G)
		print("     StrawBerry:%5d회"%S)
		print("-"*32)