import numpy as np
import cv2
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, target_x):
    result = 0
    for i in range(len(y)):
        term = y[i]
        for j in range(len(x)):
            if j != i:
                term = term * (target_x - x[j]) / (x[i] - x[j])
        result += term
    return result

def enlarge_image_lagrange_xy(original_image, scale_factor):
    # 取得影像的高度和寬度
    height, width = original_image.shape

    # 先對 x 軸進行拉格朗日插值
    x_enlarged = np.zeros((height, int(width * scale_factor)))
    for i in range(height):
        for j in range(int(width * scale_factor)):
            x = j / scale_factor
            x_enlarged[i, j] = lagrange_interpolation(np.arange(width), original_image[i, :], x)

    # 再對 y 軸進行拉格朗日插值
    y_enlarged = np.zeros((int(height * scale_factor), int(width * scale_factor)))
    for i in range(int(height * scale_factor)):
        for j in range(int(width * scale_factor)):
            y = i / scale_factor
            y_enlarged[i, j] = lagrange_interpolation(np.arange(int(width * scale_factor)), x_enlarged[:, j], y)

    # 確保灰階值在0到255之間
    enlarged_image = np.clip(y_enlarged, 0, 255).astype(np.uint8)

    return enlarged_image

# 讀取影像
#image_path = "/project/NA_proposal/image/img44.png"
#original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# or繪製簡單影像
original_image = np.array([[255,255,255,255,255],
                           [0,255,255,255,0],
                           [0,255,0,255,0],
                           [255,0,255,0,255],
                           [255,255,255,255,255]
                           ])

# 設定放大倍率
scale_factor = 2

# 進行影像放大
enlarged_image = enlarge_image_lagrange_xy(original_image, scale_factor)

# 繪製原始影像
plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Original Image')

# 繪製放大後的影像
plt.subplot(1, 2, 2)
plt.imshow(enlarged_image, cmap='gray')
plt.title('Enlarged Image')

# 顯示影像
plt.show()
