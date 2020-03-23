import sys
hrs = mns = sec = spd = res = 0
etime = stime = tmpSpd = 0
for line in sys.stdin:
    l = line.split()
    if len(l) == 2:
        spd = int(l[1])
    else:
        spd = 0
    l1 = l[0].split(":")
    hrs = int(l1[0])
    mns = int(l1[1])
    sec = int(l1[2])
    # print(hrs, mns, sec, spd)
    etime = hrs + mns / 60 + sec / 3600
    if (len(l) != 2):
        res += (etime - stime) * tmpSpd
        # print (spd, etime, stime)
        # answer = str(round(res, 2))
        print(l[0], "%.2f" % res, "km")
        # print("km", end = " ")
    else:
        res += (etime - stime) * tmpSpd
        # print ("in else")
        # print (spd, etime, stime, res)
        tmpSpd = spd
    stime = etime
# print()