from ctypes.wintypes import PHKEY
from random import * #랜덤함수 임포트

print(random()) #랜덤한 난수 등장 0.0~1.0 미만의 임의값 생성
print(random() * 10)
print(int(random()*10)) #정수형은 int 사용 0~10이하의 임의값
print(int(random()*10))
print(int(random()*10))
print(int(random()*10))
print(int(random()*10))
print(int(random()*10))
print(int(random()*10 + 1))#1~10이하의 임의값

print(int(random()*45 + 1)) #1부터45이하의 임의값
print(int(random()*45 + 1))
print("여기부터 randrange")
print(int(randrange(1, 10))) #1부터 10 미만의 임의값 
print(int(randrange(1, 11)))  
print("여기부터 randint")
print(randint(1, 45)) # 1~45이하의 임의값
print(randint(1, 45)) # 1~45이하의 임의값
print(randint(1, 45)) # 1~45이하의 임의값
print(randint(1, 45)) # 1~45이하의 임의값
print(randint(1, 45)) # 1~45이하의 임의값
print(randint(1, 45)) # 1~45이하의 임의값"이하"
#퀴즈2
studyday = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ",studyday," 일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 "+str(studyday)+" 일로 선정되었습니다.")

 
