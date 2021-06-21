n=int(input('숫자를 입력하세요:'))
FL=['Apple','Melon','Grape','StrawBerry']
FN=[3,4,5,8]
FC=[0,0,0,0]

print('==<<%d회 반복합니다>>=='%n)

for i in range(1,n+1):
	print('\n%2d.'%i,end='')
	for j in range(len(FL)):
		if(i%FN[j]==0):
			FC[j]=FC[j]+1
			print('%s'%FL[j],end='')

print('\n\n==<<Fruit Count List>>==')
for i in range(len(FL)):
	print('%d.%-12s%2d회'%(i+1,FL[i],FC[i]))