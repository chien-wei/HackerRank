from math import sqrt

T = int(input())
for i in range(T):
    num = int(input())
    if num == 0 or num == 1:
        print('Not prime')
    elif num == 2 or num == 3:
        print('Prime')
    else:
        for j in range(2, int(sqrt(num)) + 1):
            if num % j == 0:
                print('Not prime')
                break
            if j == int(sqrt(num)):
                print('Prime')