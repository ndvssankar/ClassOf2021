t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    scare_crow = 0
    j = 0
    l = len(s)
    while j < l:
        if s[j] == '.':
            scare_crow += 1
            j = j + 3
        else:
            j = j + 1
    print("Case %d: %d" % (i+1, scare_crow))