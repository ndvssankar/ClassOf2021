t = int(input())

def add(lst):
    lst = lst.split("+")
    lst = [int(i) for i in lst]
    return sum(lst)

def product(lst):
    prod = 1
    for i in lst:
        prod = prod * int(i)
    return prod

def find_max(line):
    line = line.split("*")
    res = []
    for i in line:
        if "+" in i:
            res.append(add(i))
        else:
            res.append(int(i))
    return product(res)

def find_min(line):
    line = line.split("+")
    res = []
    for i in line:
        if "*" in i:
            res.append(product(i.split("*")))
        else:
            res.append(int(i))
    return sum(res)


for i in range(t):
    line = input()
    mx = find_max(line)
    mi = find_min(line)
    print ("The maximum and minimum are {} and {}.".format(mx, mi))
