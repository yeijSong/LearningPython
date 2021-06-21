'''
실행시 2개의 값을 입력받을 예정
vid,vpwd 2개의 값
vid=Orange 이고 pwd=HappyDay이면 '반갑습니다 회원님'
아니면 '회원가입 확인하세요'
'''
vid=input("아이디를 입력하세요")
vpwd=input("비밀번호를 입력하세요")
if vid=="Orange" and vpwd=="HappyDay":
	print("반갑습니다 회원님")
else:
	print("회원가입 확인하세요")