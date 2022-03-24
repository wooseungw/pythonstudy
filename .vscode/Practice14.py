#파일 입출력
#오픈(파일명, 여는목적(w=write), utf8로 열기)
score_file = open("score.txt", "w", encoding = "utf8") 
print("수학 : 0", file=score_file)
print("도덕 : 20", file=score_file)
print("국어 : 14", file=score_file)
print("영어 : 10", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding = "utf8") #a는 덮어쓰기 apend
score_file.write("과학: 80")#줄바꿈이 따로 안됨
score_file.write("\n코딩: 80")#따로 써줘야함
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")#r은 read
print(score_file.read())#모든내용 읽기 
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")#r은 read
print(score_file.readline(),end="")#한줄만 읽기, 줄별로 '읽기'는 한줄 읽고 '커서'는 다음줄로 이동 ,end="" 줄바꿈 없애기
print(score_file.readline())#줄2
print(score_file.readline())#줄3
score_file.close()