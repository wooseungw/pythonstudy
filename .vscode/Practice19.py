def list_avg(numlist):
    sum = 0
    avg =0
    for number in numlist:
        sum += number
    avg = sum/len(numlist)
    return avg

score = [90,80,70,50,60]

print(list_avg(score))

def hello(d):
    return "hi"

a = hello("qwd")
print(a)