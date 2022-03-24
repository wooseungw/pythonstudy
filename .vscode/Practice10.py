
#퀴즈5
#50명 승객 매칭, 승객별 소요시간 5~50분 난수로 결정, 
#5~15분 사이의 승객만 매칭하기 [o] n번째 손님 (소요시간: mm분), 총 탑승 승객 : n2분
# for passenger in range(1, 51):
#     print("{0}번째 손님 (소요시간:)".format(passenger))
#모르겠어
from random import *
cnt = 0 #총 탑승 승객 수
for num in range(1,51): #1~50 이라는 승객 수
    time = randrange(5, 51) #5~50분 소요시간 랜덤
    if 5 <= time <= 15: #5~15분 이내의 손님, 탑승 cnt증가
        print("[o]  {0}번째 손님 (소요시간: {1}분".format(num, time))
        cnt += 1
    else: #cnt증가 x
        print("[ ]  {0}번째 손님 (소요시간: {1}분".format(num, time))
    if num == 50:
        print("총 탑승객 수: {0}명".format(cnt))


        

        
    
        
#
sum = 0
for i in range(1,11,1):
    sum += i*2
    print(sum)
