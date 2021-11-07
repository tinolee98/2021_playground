W,H,f,c,x1,y1,x2,y2 = list(map(int, input().split()))

result = (min(2*f, W)+x2-2*x1)*(y2-y1)*(c+1)
print(min(2*f, W)+x2-2*x1)
print(result)
# l = H//(c+1)
# print("l",l)
# count = W*H
# countX = 0
# for x in range(f+x1, f+x2):
#     if 0<=x<W:
#         countX += 1
# for x in range(f-x1-1,f-x2-1,-1):
#     if 0<=x<W:
#         countX += 1
# countY = 0
# for y in range(y1,y2):
#     for i in range(c+1):
#         y = y+l*i if i%2 == 0 else l*(i-1)-y+l
#         print(y)
#         if 0<=y<H:
#             countY += 1
# print(countX, countY)
# print(count-countX*countY)


# for x in range(f+x1, f+x2):
#     for y in range(y1, y2):
#         for i in range(c+1):
#             cx = x
#             cy = y+l*i if i%2 == 0 else l*(i+1)-y-1
#             if 0 <= cx < W and 0 <= cy < H:
#                 count -= 1
#             # print(x,y,i,cx,cy)
# # print(isColored)

# for x in range(f-x1-1, f-x2-1,-1):
#     # print(x)
#     for y in range(y1, y2):
#         for i in range(c+1):
#             cx = x
#             cy = y+l*i if i%2 == 0 else l*(i+1)-y-1
#             if 0 <= cx < W and 0 <= cy < H:
#                 # print(cx,cy)
#                 count -= 1
# # print(isColored)
# print(count)
