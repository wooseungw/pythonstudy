#피클 목표 데이터 가져와 또 쓸 수 있는것, 변수를 외부에 저장할 수 있는 바이너리
import pickle
# profile_file = open("profile.pickle", "wb")#(,바이너리 설정)\
# profile = {"이름":"우승우","나이":23, "취미":["축구","코딩","골프"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile의 정보를 file에저저장 profile.picke 파일이 생김 
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)#file정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# #'with' 파일을 열고 닫고가 편해진다
# with open("profile.pickle","rb") as profile_file:
#     print(pickle.loads(profile_file))#따로 닫을 필요 없이 with문 탈출하면서 끝남
    
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 공부하고있어요.")
    
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())