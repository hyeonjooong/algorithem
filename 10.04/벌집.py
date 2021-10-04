#10월 4일 백준 - 벌집
'''
입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.
'''
def bee(n):
    a=1 #벌집 방 시작값
    k=1 #점화식 증가값
    while True:
        if n == 1 : # 입력값이 1인 경우
            return 1
        elif n > a and n <= a + (6 * k): # 입력값이 범위 안에 속하는 경우
            return k+1
        else: # 입력값이 범위 안에 속하지 않아 범위 증가
            a = a + (6 * k)
            k += 1

n = int(input())
print(bee(n))
