import numpy as np
import math
import cv2

Magni = 2
data_x = []
data_y = []
data_z = []

# 2-norm
def norm(x,y):
    result1 = math.sqrt(math.pow(x,2)+math.pow(y,2))
    return result1

# l_j(x,y)
def l(j,x,y):
    i = 0
    result2 = 1
    for i in range(pixel):
        if i != j:
            result2 *= norm(x-data_x[i],y-data_y[i])/norm(data_x[j]-data_x[i],data_y[j]-data_y[i])
    return result2

# Lagrange(x,y)
def L(x,y):
    j = 0
    result3 = 0
    for j in range(pixel):
        result3 += data_z[j]*l(j,x,y)
    return result3




def Lagrange1(src, dst_shape):
    # 獲取原圖大小
    src_height, src_width = src.shape[0], src.shape[1]
    # 計算新圖大小
    dst_height, dst_width, channels = dst_shape[0], dst_shape[1], dst_shape[2]

    dst = np.zeros(shape = (dst_height, dst_width, channels), dtype=np.uint8)
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            # 尋找對應座標&無條件捨去
            dst_x =  int(src_x*(src_width/dst_width))
            dst_y =  int(src_y*(src_height/dst_height))

            # 插值
            dst[dst_x, dst_y,:] = L(dst_x, dst_y)
    return dst





src = cv2.imread("/project/NA_proposal/img3.png")
dst = Lagrange1(src, dst_shape=(src.shape[0]*Magni, src.shape[1]*Magni, 3))
pixel = src.shape[0]*src.shape[1]
data_x, data_y, data_z = src[0], src[1], src[2]


# 顯示

cv2.namedWindow('src', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('src', src.shape[1], src.shape[0])
cv2.imshow("src",src) 
cv2.namedWindow('dst', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('dst', dst.shape[1], dst.shape[0])
cv2.imshow("dst",dst)
cv2.waitKey(0)
