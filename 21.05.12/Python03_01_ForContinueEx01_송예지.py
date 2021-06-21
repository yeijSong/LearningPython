marks=[90,25,67,45,80]
n=0
for mark in marks:
	n=n+1
	if mark<60:
		continue
	print(n+1,'번 학생 축하합니다. 합격입니다!')
