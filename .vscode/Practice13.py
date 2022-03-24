#표준 입출력 콤마,나 +사용시 한칸 띄워서 프린트 됨 sep= 사용시 띄어쓰기 적용 비적용 뭐를 빈칸에 넣을지 선택가능 end=사용시 다음 프린트가 연쇄적으로 등장
import sys 
print("파이썬", "자바", sep=",, , ,  ", end="?")
print("파이썬", "자바")
print(" ")
print("파이썬", "자바", file=sys.stdout)#표준출력
print("파이썬", "자바", file=sys.stderr)#표준에러_확인해 프로그램 에러를 찾아야해

scores = {"수학":0, "영어":12, "코딩":22}
for subject, score in scores.items():
    print(subject.ljust(9), str(score).rjust(2), sep=":")#ljust 왼쪽정렬 rjust오른쪽 정력


#은행 대기순번표
for num in range(1,21):
    print("대기번호 : " +str(num).zfill(3))#zfill 자릿수 채우기
    
    
answer = input("아무값이나 입력하세요 :")
print(type(answer))
print("입력 값은 :"+ answer +"입니다.")#사용자 입력값은 항상 str로 

#다양한 파일 포맷 안함