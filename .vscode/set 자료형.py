employees = {"김갑수","이종팔","우총순","홍길동","김기순","오이","당근"}
employees_late = {""}
employees_skip = {""}
# print(set1)
# print(len(set1))
# print(set1 & set2)#교집합
# print(set1 - set2)#차집합
# print(set1 | set2)#합집합
employees_late.add("오이")
employees_late.add("당근")
employees_late.add("이종팔")
employees_late.add("당근")
employees_skip.add("당근")
employees_skip.add("오이")
employees_skip.add("김갑수")
employees_notbouns = employees_late | employees_skip
employees_bouns = employees - employees_notbouns
print(employees_notbouns)
print(employees_bouns)