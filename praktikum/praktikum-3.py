x1, y1 = map(int, input().split())
xs, ys = map(int, input().split())
xf, yf = map(int, input().split())

line_distance = (xf - xs)**2 + (yf - ys)**2
circle_to_finish = (xf - x1)**2 + (yf-y1)**2

if line_distance < circle_to_finish:
    print("Yes")

else:
    print("No")
