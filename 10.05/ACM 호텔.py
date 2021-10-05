#10월 5일 백준 - ACM 호텔
'''
프로그램은 표준 입력에서 입력 데이터를 받는다. 
프로그램의 입력은 T 개의 테스트 데이터로 이루어져 있는데 T 는 입력의 맨 첫 줄에 주어진다. 
각 테스트 데이터는 한 행으로서 H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다
(1 ≤ H, W ≤ 99, 1 ≤ N ≤ H × W)
'''
def acm(l):
    h = int(l[0])
    w = int(l[1])
    n = int(l[2])
    
    x = n // h
    if x < n / h:
        x += 1
    y = n - h * (x-1)
    
    
    if x < 10:
        return('{1}0{0}'.format(x,y))
    else:
        return('{1}{0}'.format(x,y))

n = int(input())
for _ in range(n):
    s = input()
    l = s.split()
    print(acm(l))
