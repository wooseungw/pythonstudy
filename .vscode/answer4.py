value  = input("문자열? ")
routine = int(input("반복횟수? "))

answer = value * routine

if routine <= 3:
    print("반복횟수가 너무 작습니다.")
elif len(value) < 5:
    if routine <= 5:
        print("{}".format(answer))
    else:
        print("반복횟수가 너무 큽니다.")
else:
    print("문자열이 너무 깁니다.")