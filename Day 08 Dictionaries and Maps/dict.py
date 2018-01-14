n = int(input().strip())
h = {}
for i in range(n):
    person = input().split()
    h[person[0]] = person[1]

try:
    while True:
        line = input().strip()
        if line in h:
            print(line + '=' + h[line])
        else:
            print('Not found')
except EOFError:
    pass


# from sys import stdin

# n = int(input().strip())
# h = {}
# for i in range(n):
#     person = input().split()
#     h[person[0]] = person[1]

# lines = stdin.readlines()
# for line in lines:
#     line = line.strip()
#     if line in h:
#         print(line + '=' + h[line])
#     else:
#         print('Not found')