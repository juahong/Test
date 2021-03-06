"""
주제 : 문자열
작성일 : 2017. 09. 06
작성자 : 홍주아
"""
# s에 "가나다라마바사아자차카타파하"를 입력
s = "가나다라마바사아자차카타파하"
print("0번째 문자 : ", s[0])
print("14번째 문자 : ",  s[13])
# 문자열 슬라이싱 활용 예
print(s[0:2])
print(s[2:4])
# ('0부터 시작한') 2부터 7까지 출력
print(s[2:8])
# 끝나는 점을 정의하지 않아도, 정의한 문자열의 끝까지 출력
print(s[5:])
# 처음부터 끝까지
print(s)
# 5에서부터 끝 바로 앞(파)까지 출력
print(s[5:-1])
# ( '\n' : 줄바꿈, '\t' : 탭 ) 이 기능을 사용하기
s_2 = "가나다라마\n바사아자차카타파하"
print(s_2)
# 심심풀이
print("\t", s[0:5], "\n", "\t", s[5:])