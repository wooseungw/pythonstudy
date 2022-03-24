#퀴즈6
#표준페중을 구하는 프로그램
#공식 남자: 키(m)x키(m)x22, 여자: 키(m)x키(m)x21
#조건1 표준체중은 별도의 함 내에서 계산
#함수명 std_weight
#전달값 키(height), 성별(gender)
#표준 체중은 소수점 둘째자리까지표시

print("practice12_Quiz#6")

# def std_weight (gender, height):
#     if gender == "남자":
#         print("키 {0}cm의 남자의 표준 체중은 {1}kg 입니다.".format(height,round(height*height*22*0.01*0.01),4))
        
#     elif gender == "여자":
#         print("키 {0}cm의 여자의 표준 체중은 {1}kg 입니다.".format(height,round(height*height*21*0.01*0.01),2))
    
#     else:
#         print("정확한 성별을 입력해주세요.")
        
# std_weight("남자", 125)
# std_weight("남자", 185)
# std_weight("남자", 175)
# std_weight("여자", 165)

def std_weight2 (gender2, height2):
    if gender2 == "남자":
        return(height2*height2*22*0.01*0.01)
    
    elif gender2 == "여자":
        return(height2*height2*21*0.01*0.01)
    
height2 = 174
gender2 = "남자"  
weight = round(std_weight2(height2/100, gender2), 2)
print("키 {0}cm의 {1}의 표준 체중은 {2}kg 입니다.".format(height2,gender2,weight))
    