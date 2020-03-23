import sys
s = ['C', 'C#', 'D','D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
d = {}
t = [2,2,1,2,2,2,1]
output = ""
for i in range(len(s)):
    l = [s[i]]
    k = i
    for j in t:
        k = k + j
        l.append(s[k%12])
    d[s[i]] = l
print (d)
for line in sys.stdin:
    res = []
    line = line[:-1]
    s = line.split(" ")
    for k in d:
        flag = True
        for c in s:
            if c not in d[k]:
                flag = False
                break
        if flag:
            res.append(k)
    output += ' '.join(res) + "\n"
print(output[:-2])
