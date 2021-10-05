#10월 5일 백준 - 설탕 배달
'''
상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.
설탕 - 3kg, 5kg
'''

def sugar(n):
    y = [i for i in range((n // 5)+1)]
    x = [i for i in range((n // 3)+1)]
    mini = -1
    for val_y in y:
        for val_x in x:
            if (3*val_x + 5*val_y) == n:
                if mini == -1:
                    mini = val_x+val_y
                elif mini > (val_x+val_y):
                    mini = val_x+val_y
    return mini

N = int(input())
print(sugar(N))
