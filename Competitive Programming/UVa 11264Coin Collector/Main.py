t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    n_coins = 1
    sum = 0
    for i in range(len(l)-1):
        if sum + l[i] < l[i+1]:
            sum += l[i]
            n_coins += 1
    print(n_coins)