#10월 6일 백준 - 소수 찾기
'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
'''
N = int(input())
num = input()
l = num.split()
result = 0

for idx in range(len(l)):
    l[idx] = int(l[idx])
    tf = True
    if l[idx] == 1:
        continue
    elif l[idx] == 2:
        result += 1
        continue
    else:
        for i in range(2,l[idx]):
            if l[idx] % i == 0:
                tf = False
                break
        if tf == True:
            result += 1
print(result)
