#함수



dogname = "댕댕이"
age = 1 #str로감싸야나온다.
hobby = "산책"
is_adult = age > 4 #str로감싸야나온다." ",," "사용시str사용안해도 돼
'''
이렇게
주석이
여러문장
가능해
범위 선택후 컨트롤 슬러쉬
'''

print(" 우리집 "+ dogname + "는 취미가 " + hobby + "이고, 나이가 "+ str(age) +" 입니다. 이정도면 어른인가요? ")
print(" " +str(is_adult) +" ")
print(" 우리집 ", dogname ,"는 취미가 ",hobby ,"이고, 나이가 ", str(age) ," 입니다. 이정도면 어른인가요? ")
#문제1
station = "김포공항"
print("",station,"행 열차가 들어오고 있습니다.")

#연산자
print(2**3) #2^3
print(10%3) #10을 3으로 나눈 나머지
print(10//3) #10을 3으로 나눈 몫
print( 10 >= 1)
print( 123 <= 3)
print( 4 <= 4 ) #크거나 같다
print( 3 == 3) #앞의 값과 뒤의 값이 같다고
print( 3%2 == 1)
print( 3 != 3) #앞과 뒤가 같지않다.
print( (3>0) and (34 < 4)) #두가지 조건이 참일 때 true
print( (3>3) & (23>4)) #and와 동일
print( (3>0) or (233> 2)) #둘중 하나만 참이면 true
print( (3>0) | (233> 2)) #둘중 하나만 참이면 true
print ( 3 < 4 < 5 )#3가지 항 비교
print("dgdd")

number = 213 * 3123
print(number)
number -= 1
print(number)
number %= 3
print(number)

print(abs(-2))
print(pow(4, 2)) #제곱
print(max(5, 12))#둘중 큰값
print(min(5, 12))#둘중 작은값
print(round(3.55555))#소숫점 버림

from math import * 
print(floor(4.66))#내림
print(ceil(3.451))#올림
print(sqrt(25))#제곱근

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

