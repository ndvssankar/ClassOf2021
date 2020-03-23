import math

def get_permutation(s, n):
    t = n % math.factorial(len(s))
    if t == 0:
        return s
    # print(s, n)
    fact = ""
    temp = n
    i = 1
    lst = []
    while temp > 0:
        r = (temp % i)
        lst.append(r)
        temp = temp // i
        i += 1
        # print (lst)
        if (len (lst) == len(s)):
            break
    
    output = ""

    
    if len(lst) < len(s):
        l = len(lst)
        # print (l)
        for i in range(len(s) - l - 1, -1, -1):
            lst.append(0)
    lst = lst[::-1]
    # print (lst)
    
    s = list(s)
    s = sorted(s)
    # print(s)
    for i in lst:
        output = output + s[i]
        # print (output)
        if (len(s) == i):
            s = s[:i-1]
        else:
            s = s[:i] + s[i+1:]
    return output

t = int(input())
for i in range(t):
    s = input()
    n = int(input())
    # print (s)
    # if  (len(s) == 2):
    output = get_permutation(s, n)
    print(output)
    # print()
    
