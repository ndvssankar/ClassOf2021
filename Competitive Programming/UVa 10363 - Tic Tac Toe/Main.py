

import sys

# if (line.count("O") == 3 or line.count("X") == 3) and not flag:
    # print("yes")

def check_tic_tac_toe(ln, x_count, o_count):
    x_count = o_count = 0
    for line in ln:
        x_count += line.count("X")
        o_count += line.count("O")
    # print (x_count, o_count)
    if (not(x_count == o_count or x_count == o_count+1)):
        return 0

    x_flag = o_flag = 0
    for i in range(3):
        if (ln[i][0] == 'X' and ln[i][0] == ln[i][1] and ln[i][1] == ln[i][2]):
            x_flag = 1
        if (ln[i][0] == 'O' and ln[i][0] == ln[i][1] and ln[i][1] == ln[i][2]):
            o_flag = 1
        if (ln[0][i] == 'X' and ln[0][i] == ln[1][i] and ln[1][i] == ln[2][i]):
            x_flag = 1
        if (ln[0][i] == 'O' and ln[0][i] == ln[1][i] and ln[1][i] == ln[2][i]):
            o_flag = 1
    if (ln[2][0] == "X" and ln[2][0] == ln[1][1] and ln[1][1] == ln[0][2]):
        x_flag = 1
    if (ln[2][0] == "O" and ln[2][0] == ln[1][1] and ln[1][1] == ln[0][2]):
        o_flag = 1
    if (ln[0][0] == "X" and ln[0][0] == ln[1][1] and ln[1][1] == ln[2][2]):
        x_flag = 1
    if (ln[0][0] == "O" and ln[0][0] == ln[1][1] and ln[1][1] == ln[2][2]):
        o_flag = 1
    
    if (x_flag and o_flag):
        return 0
    if not x_flag and not o_flag:
        return 1
    if x_flag and x_count == o_count + 1:
        return 1
    if o_flag and x_count == o_count:
        return 1
    return 0
    
    
t = int(input())
for i in range(t):
    x_count = o_count = 0
    flag = False
    line = []
    for j in range(3):
        line.append(input())
        x_count += line[j].count("X")
        o_count += line[j].count("O")
    if (i != t-1):
        input()
    if check_tic_tac_toe(line, x_count, o_count):
        print ("yes")
    else:
        print ("no")
    # print (x_count, o_count)

