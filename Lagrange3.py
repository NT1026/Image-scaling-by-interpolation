import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from PIL import Image

def resize_image(image_path, scale_factor):
    # 讀取圖片
    img = Image.open(image_path).convert('L')  # 將圖片轉為灰階

    # 獲取圖片數據
    img_array = np.array(img)

    # 獲取圖片大小
    height, width = img_array.shape

    # 生成原始數據點坐標
    x = np.arange(0, width)
    y = np.arange(0, height)

    # 將x軸擴大
    new_width = int(width * scale_factor)
    new_x = np.linspace(0, width - 1, new_width)

    # 生成新的坐標點
    new_y = np.arange(0, height - 1 + (1/scale_factor), 1/scale_factor)

    # 進行二維拉格朗日插值
    new_img_array = np.zeros((len(new_y), new_width))
    for i in range(len(new_y)):
        for j in range(new_width):
            # 修正索引超出範圍的問題
            if i < height:
                coefficients_x = lagrange(x, img_array[i, :])
                new_img_array[i, j] = coefficients_x(new_x[j])

    # 設定圖片大小
    plt.figure(figsize=(10, 5))

    # 顯示原始圖片
    plt.subplot(1, 2, 1)
    plt.imshow(img_array, cmap='gray')
    plt.title('Original Image')

    # 顯示放大後的圖片
    plt.subplot(1, 2, 2)
    plt.imshow(new_img_array, cmap='gray')
    plt.title('Resized Image')

    # 顯示放大後的圖片大小
    plt.text(1.05, 0.5, f"New Size: {new_img_array.shape[1]} x {new_img_array.shape[0]}", verticalalignment='center', transform=plt.gca().transAxes)

    plt.show()

    return new_img_array

# 指定圖片路徑和放大倍數
image_path = '/project/NA_proposal/img1.png'
scale_factor = 2  # 修改為你需要的放大倍數

# 呼叫函數進行圖片放大
resized_image = resize_image(image_path, scale_factor)
