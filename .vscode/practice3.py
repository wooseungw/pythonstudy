#문자열
sentence = '나는 소년 입니다.'
print(sentence) 
sentence2 = """
만남은 쉽고
이별을 어려워어어
"""
print(sentence2)
#슬라이싱=대괄호
juminnumber = "970708-1123141"
print("성별 : " +juminnumber[7])
print("연생 : " +juminnumber[0:2])#[0번부터 시작 , 필요한 자리수 +1만큼][0,2](0,1)번 출력
print("생년월일 : " + juminnumber[:6])#처음부터 6자리 직전까지
print("뒷자리 : " + juminnumber[7:14])#시작하는 자리와 끝자리를 계산하기
print("뒷자리 : " + juminnumber[7:])
print("뒷자리 : (뒤부터)" + juminnumber[-7:])#맨뒤부터 7자리

python = "Pyhton is Amazing"
print(python.lower())#소문자 출력
print(python.upper())#대문자 출력
print(python[0].isupper())#0번째 자리가 upper인가?
print(len(python))#길이 숫자로 표현
print(python.replace("Pyhton ", "Java "))#단어대체
index = python.index("n")#n이라는 글자 몇번째에 있는지
print(index)
index = python.index("n", index + 1)#두번째n이몇번째에있는지
print(index)

print(python.find("n"))#첫번째 n찾아줌 없는값은 -1로 출력됨
print(python.index("is"))#없는 값은 안나옴

#문자열 포맷
print("a"+"b")
print("a", "b")

print("나는 %d살입니다." % 20)#d는 정수값만 
print("나는 %s살입니다." % 123)#s는 글자도rp
print("나는 %c살입니다." % "a")#c는 한 글자만

print("나는 %s와 %s를 좋아해요" %("우리","나"))#괄호 사용

print("나는 {}살입니다.".format(20))
print("나는 {}와 {}를 좋아해요".format("우리","나"))
print("나는 {1}와 {0}를 좋아해요".format("우리","나"))#중괄호 안 숫자 바꾸는 거로 순서변경도 가능

print("나는 {age}살이며,{like}를 좋아해요".format(age = 10 , like= "우리"))#중괄호안에 변수명 넣어주기
print("나는 {like}살이며,{age}를 좋아해요".format(age = 10 , like= "우리"))

age = 20
color = "파랑검은빨강"
print(f"나는 {age}살이며,{color}를 좋아해요") 

#탈출문장 = \n, \" \", \\
print("탈출문장")
print("백문이 불여일견 \n 백견이 불여일타")
print("나는 '나는코딩'입니다.")
print('나는 "나는코딩"입니다.')
print("나는 \"나는코딩\"입니다.") # \" \"

# \\ : 문장 내 하나의\로 바뀐다.
print("아아\\로")
# \r 커서 맨 앞으로 이동
print("사과 애플 \r파인")
#\b 백스페이스
print("reD\b Apple")
# \t =tab
print("red \t apple")
#quiz 3 사이트별 비밀번호 만들어주는 프로그램 작성 1:17:02

# Site = 'https://www.naver.com'
# SiteRemove = Site[12:]
# SiteRemoveBackside = SiteRemove[:]
# Passwordfront = SiteRemove[0:3]
# Passwordmiddle = len(SiteRemoveBackside) 
# print(f"생성된 비밀번호는 \"{Passwordfront}{Passwordmiddle}!\"입니다. ")

#정답
url = "https://www.instagram.com/"
my_str = url.replace("https://www." , "")#규칙1
print(my_str)
my_str = my_str[:my_str.index(".")]#규칙2_★[:처음나오는 "."의 위치까지] 
print(my_str)
Password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, Password))