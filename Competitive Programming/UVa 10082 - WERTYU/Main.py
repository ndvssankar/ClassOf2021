import sys
wrong = ["WERTYUIOP[]1234567890-=", "SDFGHJKL;'" ,"XCVBNM,./"]
corre = ["QWERTYUIOP[]1234567890-=","ASDFGHJKL;'","ZXCVBNM,."]

def get_correct_string(line):
    res = ""
    for i in line:
        flag = False
        if i == " ":
            res = res + ' '
            flag = True
        elif i == '/':
            res = res + '.'
            flag = True
        elif i == '\\':
            res = res + ']'
            flag = True
        elif i == '1':
            res = res + '`'
            flag = True
        else:
            for j in range(len(wrong)):
                if wrong[j].find(i) != -1:
                    idx = wrong[j].find(i)
                    res = res + corre[j][idx]
                    flag = True
                    break
        if flag == False and i != '\n':
            res = res + i
    return res
for line in sys.stdin:
    s = get_correct_string(line)
    print(s)