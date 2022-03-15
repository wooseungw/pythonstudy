#한출for문
students = [1,2,3,4,5,6,7,8,9]
print(students)
students = [i+100 for i in students]#i에 100더한값을 넣어라 i는 students에 있는거
print(students)

#학생이름 길이로 변환
studentsname = ["fqfwwww", "fwqwwwgfsdb", "dfwwwee","gwgwgwwg"]
# studentsname = [len(i2) for i2 in studentsname]
# print(studentsname)

#학생이름 대문자로
studentsname = [i3.upper() for i3 in studentsname]
print(studentsname)

#퀴즈5
#50명 승객 매칭, 승객별 소요시간 5~50분 난수로 결정, 5~15분 사이의 승객만 매칭하기 [o] n번째 손님 (소요시간: mm분), 총 탑승 승객 : n2분