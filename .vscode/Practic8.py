#Continue, Break
Absent = [1,5]#결석 결석자 빼고 계속 = Continue
Nobook = [21]
for student in range(1, 30):
      if student in Absent:
            continue#다음 반복으로 계속
      elif student in Nobook:
            print("{0}번 너 나와".format(Nobook))
            break#바로 반복문 탈출
      print("{0}번 책 읽어봐".format(student))