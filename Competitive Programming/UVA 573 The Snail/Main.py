while True:
    test_list = list(map(int, raw_input().split(" ")))
    h = test_list[0]
    if h == 0:
        break
    u = test_list[1]
    d = test_list[2]
    f = test_list[3]
    days = 0
    initialHeight = 0.0
    distanceClimbed = u
    heightAfterClimbing = u
    heightAfterSliding = heightAfterClimbing - d
    fatigueFactor = u * (f / 100.0)
    print days, " :: " , initialHeight, " :: " , distanceClimbed , " :: " , heightAfterClimbing , " :: " , heightAfterSliding
    while True:
        days = days + 1
        if (days == 1):
            pass
        else:
            initialHeight = heightAfterSliding
            distanceClimbed = distanceClimbed - fatigueFactor
            if distanceClimbed <= 0:
                distanceClimbed = 0
            
            heightAfterClimbing = initialHeight + distanceClimbed
            heightAfterSliding = heightAfterClimbing - d
            print days, " :: " , initialHeight, " :: " , distanceClimbed , " :: " , heightAfterClimbing , " :: " , heightAfterSliding
        if heightAfterClimbing > h:
            print "success on day" , days
            break
        
        if heightAfterSliding < 0:
            print "failure on day" , days
            break
