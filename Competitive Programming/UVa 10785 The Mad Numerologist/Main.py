v = "AUEOI"
vowels = []
for vowel in v:
    vowels += [vowel] * 21

c = "JSBKTCLDMVNWFXGPYHQZR"
consonants = []

for consonant in c:
    consonants += [consonant] * 5

n_tests = int(input())
for t in range(n_tests):
    vlst = []
    clst = []
    n = int(input())
    
    vlst = vowels[0:n//2]
    clst = consonants[0:n//2]

    if n % 2:
        vlst.append(vowels[n//2])
    vlst.sort()
    clst.sort()
    
    flag = False
    c = 0
    v = 0
    res = []
    # res = "".join(a+b for a,b in zip(vlst, clst))
    for i in range(n):
        if flag == False and v < len(vlst):
            res.append(vlst[v])
            flag = True
            v += 1
        else:
            if c < len(clst):
                res.append(clst[c])
                flag = False
                c += 1
    res = "Case " + str(t+1) + ": " + "".join(res)
    print (res)