import datetime

def divider():
    x = datetime.datetime.now()
    print('======'+x.strftime("%Y%m%d %H:%M:%S")+'======')

def hello():
    print('HEllo World!!!')

def nine_nine():
    for i in range(1, 10):
        for j in range(1, 10):
            print("%d X %d = %2d" % (i,j,i*j), end="  ")
        print("")