'''
p112 Q1,2
'''

scores=[80,75,55]
sum=0
for score in scores:
	sum=sum+score
	
print('홍길동님의 평균 점수는',sum/len(scores),'점 입니다')


n=int(input('숫자를 입력해주세요:'))
if n%2==1:
	print('홀수입니다')
elif n%2==0:
	print('짝수입니다')
'''
print(13%2)