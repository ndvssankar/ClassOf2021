import sys

for line in sys.stdin:
    # print (line, type(line))
    h = int(line[0:2])
    m = int(line[2:4])
    s = int(line[4:6])
    c = int(line[6:8])
    
    ms = c * 10 + s * 1000 + m * 60000 + h * 3600000
    h = ms // 8640000
    ms = ms % 8640000

    m = ms // 86400
    ms = ms % 86400

    s = ms // 864
    ms = ms % 864

    c = (ms * 100) // 864
    res = str(h)
    if m < 9:
        res += "0"
    res += str(m)
    if s < 9:
        res += "0"
    res += str(s)
    if c < 9:
        res += "0"
    res += str(c)
    # res = str(h) + str(m) + str(s) + str(c)
    print(res)