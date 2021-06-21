
# Q1

print('Q1')

scores=[80,75,55]
sum=0
for score in scores:
	sum=sum+score
	
print('홍길동님의 평균 점수는',sum/len(scores),'점 입니다')
print()

# Q2
print('Q2')
n=int(input('숫자를 입력해주세요:'))
if n%2==1:
	print('홀수입니다')
elif n%2==0:
	print('짝수입니다')
print()

# Q3 홍길동 주민등록번호: 881120-1068234
print('Q3')

a='881120-1068234'
yyyymmdd=a[0:6]
n=a[7:]
print('홍길동 님의 생년월일은',yyyymmdd,'입니다.')
print('주민등록번호의 나머지 부분은',n,'입니다.')
print()


# Q4.주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별. 그 부분을 출력해보자.
print('Q4')

pin='881120-1068234'

if pin[7]==1 or 3:
	print('남성입니다')

elif pin[7]==2 or 4:
	print('여성입니다')
print()


# Q5 replace활용하여 a:b:c:d를 a#b#c#d로 바꾸기
print('Q5')
i='a:b:c:d'
j=i.replace(':','#')
print(j)
print()


# Q6 [1,3,5,4,2]를 [5,4,3,2,1]로 바꾸기
print('Q6')
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
print()


# Q7 ['Life','is','too','short']를 Life is too short로 바꾸기
print('Q7')
a=['Life','is','too','short']
b=' '.join(a)
print(b)
print()


# Q8 (1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)로 바꾸기
print('Q8')
a=(1,2,3)
b=(4,)
print(a+b)
print()


'''
# Q9 다음과 같은 딕셔너리 a가 있다. 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
a = dict()
>>> a
{}
1. a['name'] = 'python'
2. a[('a',)] = 'python'
3. a[[1]] = 'python'
4. a[250] = 'python'

'''

print('Q9')
print('오류가 발생하는 것은 3번이다. 값이 변화할 수 있는 리스트를 key값으로 사용할 수 없기 때문이다.')
print()


# Q10 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.

print('Q10')
a = {'A':90, 'B':80, 'C':70}
b=a.pop('B')
print('B의 값은',b)
print()


# Q11 a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print('Q11')
b=set(a)
print(b)
c=list(b)
print(c)
print()


# Q12 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까? 그 이유는?
a = b = [1, 2, 3]
a[1] = 4
print('Q12')

print('변경 후 a:',a)
print('변경 후 b:',b)
print()
print('b를 출력해보면 a와 동일한 결과가 나타난다는 것을 알 수 있다.')
print()
print(id(a))
print(id(b))
print('a와b의 위치를 확인해봐도 동일한 것을 알 수 있다.')
print()
print('a와b는 동일한 객체를 가리키고 있기 때문에 변경 후에도 동일한 객체를 가리킨다.')