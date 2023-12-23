import cv2
import numpy as np

src = cv2.imread("images/img.png")

magni = 2
# Original image size
src_height = src.shape[0]
src_width = src.shape[1]

# New image size
dst_height = src.shape[0] * magni
dst_width = src.shape[1] * magni
channels = 1

dst = np.zeros(
    shape=(dst_height, dst_width, channels), 
    dtype=np.uint8
)

# Interpolation
for dst_x in range(dst_height):
    for dst_y in range(dst_width):
        if (int(dst_x / magni) == dst_x / magni) and (int(dst_y / magni) == dst_y / magni):
            src_x = int(dst_x / magni)
            src_y = int(dst_y / magni)
            dst[dst_x, dst_y, :] = src[src_x, src_y, :]
