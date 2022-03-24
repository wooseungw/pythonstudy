#함수, 전달갑과 반환값



def open_account(): #함수 정의 def 함수명():
    print("새로운 계좌가 생성되었습니다.")
    
open_account()#함수 정의 후 선언 해야 출력됨

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은{0}원 입니다.".format(balance - money))
    else:
        print("출금이 완료되지 않았습니다. 잔액:{0}".format(balance))
        
def withdraw_night(balance, money):       
    commission = 100
    return commission, balance - money - commission #여러개 값 한번에 반환가능



balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 300)
commission, balance = withdraw_night(balance, 300)
print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission, balance))
print(balance)

# 기본값 함수 정의시 값을 지정할 수 있음
def profile(name, age = 17, main_lang = "파이썬"):
     print("이름: {0}\t나이: {1} \t사용언어:{2}".format(name, age, main_lang))
     
profile("우승우", 21, "없음")
profile("우우승", 25, "없음")
profile("기본값")

#키워드 값 이용 함수호출
def profile2(name, age, main_lang):
    print(name, age, main_lang)
    
profile2(name= "dndmdm", main_lang = "dfwww",age = 12)#뒤죽박죽이어도 이름만 맞으면 된다.
#가변인자 이용 함수호출
def profile3(name, age, lang, lang1, lang2, lang3):
    print("이름: {0}\t나이: {1}".format(name,age), end =" ")
    print(lang, lang1, lang2, lang3)
    
profile3("우재석", 72, "파이선", "씨샵", "더페이스샵", "샵옆샵")
profile3("김태후", 14, "스위푸투", "오잉", "", "")#매번 빈칸을 만들어야 된다., 아니면 함수를 변형애햐하는데 이때 가변인자 이용가능

def profile4(name, age, *language):#가변인자 사용 *사용
    print("이름: {0}\t나이: {1}".format(name,age), end =" ")
    for lang in language:
        print(lang,end=" ")
    print()
    
profile4("재스기", 22, "씨샵", "더페이스샵", "으으우아아", "샵옆샵")
profile4("김태후", 14, "스위푸투", "오잉")

#'지역변수' 함수내 사용 '전역변수' 모든 프로그램 내 사용가능
gun = 10

def checkpoint(soilders):
    global gun #전역변수 gun을 함수 내에서 사용 'global' 가급적 전역변수는 사용 자제
    gun = gun - soilders#여기는 함수 내의 gun을 말하는 것
    print("함수 내에서 남은 총: {0}".format(gun))
    
def checkpoint_re(gun, soilders):
    gun = gun -soilders
    print("함수 내에서 남은 총: {0}".format(gun))
    return#바뀐 변수gun 전역으로 리턴
    
print("전체 총 개수:{0}".format(gun))
checkpoint(2)
print("남은 총 개수:{0}".format(gun))

