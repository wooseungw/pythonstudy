#IF문 
weather = input("오늘 날씨는 어때요?")#input 사용자의 대답을 기다림(터미널에 입력)
if weather == "비" or "눈":                 #조건 0, or사용시 앞조건 혹은 뒷조건 하나만 만족해도 됨
      print("우산을 챙기세요") #실행명령문
elif weather == "미세먼지":          #조건 1
      print("마스크를 챙기세요")
else:                               #모든 조건이 없을 때 else사용
      print("준비물 필요 없어요.")
      
temp = int(input("기온은 어때요? "))#정수형이라 int로 감쌈
if 30 <= temp:
      print("반팔을 입으세요.")
elif 10 <= temp < 30: 
      print("긴팔을 입으세요")
# elif 10 <= temp and temp < 30: #and사용시 앞과 뒤 조건 모두 만족해야함
#       print("긴팔을 입으세요")
elif 0 <= temp and temp < 10:  
      print("두꺼운 옷을 입으세요")
else:
      print("나가지 마세요")
      
#for(반복문)
      
