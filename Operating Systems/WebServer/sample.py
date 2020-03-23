import sys
t = int(input())
l = []
i = 2
for line in sys.stdin:
    # n = int(input())
    n = int(line)
    l.append(n)
    if i == 0:
        i = 1
        print(n)
        temp = n
    else:
        # print (l, l[-2])
        print ((n - l[-2]) // t)
        temp = n