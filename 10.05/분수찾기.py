#10월 5일 백준 - 분수찾기
'''
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
'''

def fraction(n):
    k = 2 # k=2부터 시작
    Bk = 2 #B2 = 2로 시작
    while True:
        if n == 1: #k=1일 경우
            return "1/1"
        elif Bk <= n < Bk + k: 
            if k % 2 == 0: # 짝수일 경우
                return "{0}/{1}".format(1 + (n - Bk) , k - (n - Bk))
            else: #홀수일 경우
                return "{0}/{1}".format(k - (n - Bk) , 1 + (n - Bk))
        else:
            Bk += k
            k += 1


n = int(input())
print(fraction(n))
