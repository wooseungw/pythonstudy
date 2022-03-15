#While (반복문2)
#starbucks = ["철수", "영희", "바둑이","ㄴㄴ"]
# customer = "야야"
# index = 5
# while index >= 1:
#       print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#       index -= 1
#       if index == 0:
#             print("커피 버렸어")
            
# customer2 = "여여"
# index2 = 1
# while True:
#       print("{0}, 커피가 준비됨 {1}번 불렀어".format(customer2, index2))
#       index2 += 1
#       if index2 == 10:
#             print("커피 알아서 가져가")

from operator import index


customer = "나나"
person = "Unknown"

while person != customer :
      print("{0}, 커피준비 완. ".format(customer))
      person = input("이름이 어떻게 되세요?")
      