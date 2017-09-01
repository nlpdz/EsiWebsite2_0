# -*- coding:utf-8 -*-
def daterange():
    import time
    data = time.strftime('%Y %m %d', time.localtime(time.time()))
    y, m, d = data[:4], data[5:7], data[8:]
    mist = ["02", "04", "06", "08", "10", "12"]
    dist = ["31", "31", "28", "30", "30", "31"]
    m1 = int(m)
    y1 = int(y)
    mstart = "1"
    daystart = "1"
    yend = y
    if m1 >= 1 and m1 < 3:
        # 16.10.31
        mend = mist[4]
        ystart = y1 - 11
        yend = str(y1 - 1)
        dayend = dist[0]
    elif m1 >= 3 and m1 < 5:
        # 16.12.31
        mend = mist[5]
        ystart = y1 - 11
        yend = str(y1 - 1)
        dayend = dist[1]
    elif m1 >= 5 and m1 < 7:
        # 17.02.28
        mend = mist[0]
        ystart = y1 - 10
        # 运算符优先级 not > and > or
        if y1 % 100 != 0 and y1 % 4 == 0 or y1 % 400 == 0:
            dayend = "29"
        else:
            dayend = dist[2]
    elif m1 >= 7 and m1 < 9:
        mend = mist[1]
        ystart = y1 - 10
        dayend = dist[3]
    elif m1 >= 9 and m1 < 11:
        mend = mist[2]
        ystart = y1 - 10
        dayend = dist[4]
    else:
        mend = mist[3]
        ystart = y1 - 10
        dayend = dist[5]
    startdata = str(ystart) + "-01-01"
    enddata = yend + "-" + mend + "-" + dayend
    return startdata,enddata

