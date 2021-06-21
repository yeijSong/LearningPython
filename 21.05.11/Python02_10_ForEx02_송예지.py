scores=[90,25,67,45,80]

n=0
for score in scores:
	n=n+1
	if score>=60:
		print(n,"번 학생은 합격입니다")
	else:
		print(n,"번 학생은 불합격입니다")