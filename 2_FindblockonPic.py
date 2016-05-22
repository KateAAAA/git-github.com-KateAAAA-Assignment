import cv2
import math

src = cv2.imread("norm.png", cv2.IMREAD_GRAYSCALE)

thresh = 0
maxValue = 255

th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);
cv2.imshow("ex1",dst)
cv2.waitKey()





height, width = dst.shape[:2]

px =[];
py=[];

count =0;
for x in range(0, height):
    for y in range(0, width):        
        if(dst[x,y] <1):
            px.append(x)
            py.append(y)
            count = count+1;
             
print (count);

for t in range(0, count-1):
    rx =math.fabs(px[t]-px[t+1]);
    ry =math.fabs(py[t]-py[t+1]);
    if (rx>25 or ry>25):
        mx = px[t+1];
        my = py[t+1]


print my, mx
