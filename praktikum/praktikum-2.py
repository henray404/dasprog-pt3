x, y = map(int, input().split())
XA, YA = map(int, input().split())
M = int(input())

if (XA == 0 and YA == 0) or (XA == x and YA == y) or (XA == 0 and YA == y) or (XA == x and YA == 0):
    ubin = 3
elif XA == 0 or YA == 0 or XA == x or YA == y:
    ubin = 5
else:
    ubin = 8

if M == 0:
    ubin = 0
elif M == 1:
    x1, y1 = map(int, input().split())
elif M == 2:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
elif M == 3:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if (XA+1 == x1 or XA-1 == x1) or (YA+1 == y1 or YA-1 == y1):
        ubin -= 1
    if (XA+1 == x2 or XA-1 == x2) or (YA+1 == y2 or YA-1 == y2):
        ubin -= 1
    if (XA+1 == x3 or XA-1 == x3) or (YA+1 == y3 or YA-1 == y3):
        ubin -= 1
elif M == 4:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    if (XA+1 == x1 or XA-1 == x1) or (YA+1 == y1 or YA-1 == y1):
        ubin -= 1
    if (XA+1 == x2 or XA-1 == x2) or (YA+1 == y2 or YA-1 == y2):
        ubin -= 1
    if (XA+1 == x3 or XA-1 == x3) or (YA+1 == y3 or YA-1 == y3):
        ubin -= 1
    if (XA+1 == x4 or XA-1 == x4) or (YA+1 == y4 or YA-1 == y4):
        ubin -= 1
elif M == 5:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    if (XA+1 == x1 or XA-1 == x1) or (YA+1 == y1 or YA-1 == y1):
        ubin -= 1
    if (XA+1 == x2 or XA-1 == x2) or (YA+1 == y2 or YA-1 == y2):
        ubin -= 1
    if (XA+1 == x3 or XA-1 == x3) or (YA+1 == y3 or YA-1 == y3):
        ubin -= 1
    if (XA+1 == x4 or XA-1 == x4) or (YA+1 == y4 or YA-1 == y4):
        ubin -= 1
    if (XA+1 == x5 or XA-1 == x5) or (YA+1 == y5 or YA-1 == y5):
        ubin -= 1
elif M == 6:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    x6, y6 = map(int, input().split())
    if (XA+1 == x1 or XA-1 == x1) or (YA+1 == y1 or YA-1 == y1):
        ubin -= 1
    if (XA+1 == x2 or XA-1 == x2) or (YA+1 == y2 or YA-1 == y2):
        ubin -= 1
    if (XA+1 == x3 or XA-1 == x3) or (YA+1 == y3 or YA-1 == y3):
        ubin -= 1
    if (XA+1 == x4 or XA-1 == x4) or (YA+1 == y4 or YA-1 == y4):
        ubin -= 1
    if (XA+1 == x5 or XA-1 == x5) or (YA+1 == y5 or YA-1 == y5):
        ubin -= 1
    if (XA+1 == x6 or XA-1 == x6) or (YA+1 == y6 or YA-1 == y6):
        ubin -= 1
elif M == 7:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    x6, y6 = map(int, input().split())
    x7, y7 = map(int, input().split())
    if (XA+1 == x1 or XA-1 == x1) or (YA+1 == y1 or YA-1 == y1):
        ubin -= 1
    if (XA+1 == x2 or XA-1 == x2) or (YA+1 == y2 or YA-1 == y2):
        ubin -= 1
    if (XA+1 == x3 or XA-1 == x3) or (YA+1 == y3 or YA-1 == y3):
        ubin -= 1
    if (XA+1 == x4 or XA-1 == x4) or (YA+1 == y4 or YA-1 == y4):
        ubin -= 1
    if (XA+1 == x5 or XA-1 == x5) or (YA+1 == y5 or YA-1 == y5):
        ubin -= 1
    if (XA+1 == x6 or XA-1 == x6) or (YA+1 == y6 or YA-1 == y6):
        ubin -= 1
    if (XA+1 == x7 or XA-1 == x7) or (YA+1 == y7 or YA-1 == y7):
        ubin -= 1
elif M == 8:
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    x5, y5 = map(int, input().split())
    x6, y6 = map(int, input().split())
    x7, y7 = map(int, input().split())
    x8, y8 = map(int, input().split())
    if (XA+1 == x1 or XA-1 == x1) or (YA+1 == y1 or YA-1 == y1):
        ubin -= 1
    if (XA+1 == x2 or XA-1 == x2) or (YA+1 == y2 or YA-1 == y2):
        ubin -= 1
    if (XA+1 == x3 or XA-1 == x3) or (YA+1 == y3 or YA-1 == y3):
        ubin -= 1
    if (XA+1 == x4 or XA-1 == x4) or (YA+1 == y4 or YA-1 == y4):
        ubin -= 1
    if (XA+1 == x5 or XA-1 == x5) or (YA+1 == y5 or YA-1 == y5):
        ubin -= 1
    if (XA+1 == x6 or XA-1 == x6) or (YA+1 == y6 or YA-1 == y6):
        ubin -= 1
    if (XA+1 == x7 or XA-1 == x7) or (YA+1 == y7 or YA-1 == y7):
        ubin -= 1
    if (XA+1 == x8 or XA-1 == x8) or (YA+1 == y8 or YA-1 == y8):
        ubin -= 1


if ubin > 0:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")
