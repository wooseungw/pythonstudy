#리스트
#지하철 칸별로 10명, 20명, 30명 있다고할때 변수에 따로 저장안하고 하나의 변수로 묶는것
#자료형 섞여도 괜찮음
from calendar import c
from re import S, sub
from ssl import ALERT_DESCRIPTION_ACCESS_DENIED

#리스트
subway = ["가가가가", "나나나", "다다다다", "라라라라"]
print(subway.index("라라라라")) #index는 문자열에서 배움
subway.append("아아아아")
print(subway)
subway.insert(1, "오어어어")
print(subway)
subway.pop() #하나가 빠짐
print(subway)
subway.pop() #하나가 빠짐
print(subway)
subway.pop() #하나가 빠짐
print(subway)

subway.append("가가가가")
print(subway)
print(subway.count("가가가가"))
#정렬
num = [1,2,3,56,2,2,3,3,4,12,]
num.sort()
print(num)
#뒤집기 정렬
num.reverse()
print(num)
#num.clear()  #리스트 삭제
 
subway.extend(num) #리스트 합치기
print(subway) 

#(사전): 키와 벨류 형태 {}중괄호 사용, 사전에 키 없는걸 프린트하면 프로그램 종료됨 
cabinet = {"A-3":"유재석","B-2":"김태우"} #{키:벨류}
print(cabinet["A-3"])
print(cabinet["A-3"])

print(cabinet.get(3))#이렇게도 자료를 가져올수있음 get사용시 없는 키 프린트 해도 프로그램 종료x
print(cabinet.get(4))
print(cabinet.get(4,"사용 가능ㅋ"))
#사전 자료형 안에 값이 있는지 확인하는법
print(3 in cabinet)#(값 in 사전)
print("A-3" in cabinet)#(값 in 사전)
#새로운 자료 넣기
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "강호동" #대체도 가능
print(cabinet)

#자료 제거
del cabinet["B-2"]
print(cabinet)

#key만 출력 ,value만 출력,  쌍으로 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 모든 값 지우기
cabinet.clear()
print(cabinet)

#'튜플' 내용변경x list보다 처리속도가 빠름
(name, age, hobby) = ("나", 20 , "코딩")
print(name, age, hobby)
#리스트
menu = ("돈까스", "치즈까스") 
print(menu[0])
print(menu[1])



#세트 = 집합 {}중괄호 사용
my_set = {1,2,3,4,5,1,2}
print(my_set) #list와 달리 중복허용하지 않음 , 추가,제거는 가능

java = {"유재석", "김태호오", "양세찬"}
python = set(["유재석", "박명수"])

#교집합찾기     & .intersection
print(java & python)
print(java.intersection(python))
#합집합 | .union
print(java.union(python))
print(java | python)
#차집합 
print(java - python)
print(java.difference(python))
#세트 값 추가 제거
python.add("김태호오")
print(python)
python.remove("김태호오")
print(python)

#자료구조 변경
menu2 = {"커피", "우유", "주스"}
print(menu2, type(menu))#type은 자료형의 class를 알려줌

menu2 = list(menu2)
print(menu2, type(menu))

menu2 = tuple(menu2)
print(menu2, type(menu))

menu2 = set(menu2)
print(menu2, type(menu))

#퀴즈3
from random import *
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list)
shuffle(list)
print(list)
dak = list[0]
list.pop(0)
coffee = sample(list, 3)
print("""당첨자 발표
      치킨 당첨자:{0}
      커피 당첨자:{1}
      축하합니다.""".format(dak, coffee))
list.pop()