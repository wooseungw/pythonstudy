score = int(input("중간고사 성적? "))
absent = int(input("결석 횟수? "))

if score < 60 or absent >= 3:
    print("경고를 받는다.")
else:
    print("경고를 받지 않는다.")