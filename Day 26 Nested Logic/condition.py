[da, ma, ya] = [int(x) for x in input().split()]
[de, me, ye] = [int(x) for x in input().split()]
count = 0

if (ya > ye):
    count += 10000
elif (ya == ye and ma > me):
    count += 500 * (ma - me)
elif (ma == me and da > de):
    count += 15 * (da - de)
    
print(count)