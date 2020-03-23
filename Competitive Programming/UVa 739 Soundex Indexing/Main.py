import sys

def get_code(ch):
    if ch not in ['A','E','I','O','U','Y','W','H']:
        if ch in ['B','P','F','V']:
            return '1'
        elif ch in ['C','S','K','G','J','Q','X','Z']:
            return '2'
        elif ch in ['D','T']:
            return '3'
        elif ch in ['L']:
            return '4'
        elif ch in ['M','N']:
            return '5'
        elif ch in ['R']:
            return '6'
    return ""

def check_immediate_letters(line, i):
    # print(line, i, i+1)
    if (i < len(line)) and line[i] == line[i-1]:
        return False
    elif (i < len(line)):
        a = get_code(line[i])
        b = get_code(line[i-1])
        if a == b:
            return False
    return True

def parse(line):
    s = line[0]
    i = 1
    flag = True
    while i < len(line):
        flag = check_immediate_letters(line, i)
        if flag == True and line[i] != '\n':
            s = s + get_code(line[i])
        i = i + 1
        if (len(s) == 4):
            break
    for i in range(len(s), 4):
        s = s + '0'
    s = line[0:-1] + ";" + s
    print(s)



for line in sys.stdin:
    parse(line)

