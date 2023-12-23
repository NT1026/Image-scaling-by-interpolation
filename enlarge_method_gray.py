import numpy as np


def nearest_neighbor(src, dst_shape, magni):  
    # New image size
    dst_height = dst_shape[0]
    dst_width = dst_shape[1]
    channels = dst_shape[2]

    dst = np.zeros(
        shape=(dst_height, dst_width, channels), 
        dtype=np.uint8
    )

    # Interpolation
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            src_x = int(dst_x / magni)
            src_y = int(dst_y / magni)
            
            dst[dst_x, dst_y] = src[src_x, src_y]

    return dst


def bilinear_interpolation(src, dst_shape, magni):
   # New image size
    dst_height = dst_shape[0]
    dst_width = dst_shape[1]
    channels = dst_shape[2]

    dst = np.zeros(
        shape=(dst_height, dst_width, channels), 
        dtype=np.uint8
    )

    # Interpolation
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            if (int(dst_x / magni) == dst_x / magni) and (int(dst_y / magni) == dst_y / magni):
                (src_x, src_y) = (int(dst_x / magni), int(dst_y / magni))
                dst[dst_x, dst_y] = src[src_x, src_y]

    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            if int(dst_x / magni) == dst_x / magni:
                (a_x, a_y) = (int(dst_x / magni) * magni, int(dst_y / magni) * magni)
                (b_x, b_y) = (int(dst_x / magni) * magni, int(dst_y / magni) * magni + magni)
                if b_x > dst_height - 1 or b_y > dst_width - 1:
                    continue
                dst[dst_x, dst_y] = min(dst[a_x, a_y], dst[b_x, b_y]) + (max(dst[a_x, a_y], dst[b_x, b_y]) - min(dst[a_x, a_y], dst[b_x, b_y])) * (dst_y - a_y) / magni
            elif int(dst_y / magni) == dst_y / magni:
                (a_x, a_y) = (int(dst_x / magni) * magni, int(dst_y / magni) * magni)
                (b_x, b_y) = (int(dst_x / magni) * magni, int(dst_y / magni) * magni + magni)
                if b_x > dst_height - 1 or b_y > dst_width - 1:
                    continue
                dst[dst_x, dst_y] = min(dst[a_x, a_y], dst[b_x, b_y]) + (max(dst[a_x, a_y], dst[b_x, b_y]) - min(dst[a_x, a_y], dst[b_x, b_y])) * (dst_x - a_x) / magni

    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            if (int(dst_x / magni) != dst_x / magni) and (int(dst_y / magni) != dst_y / magni):
                (a_x, a_y) = (dst_x, int(dst_y / magni) * magni)
                (b_x, b_y) = (dst_x, int(dst_y / magni) * magni + magni)
                if b_x > dst_height - 1 or b_y > dst_width - 1:
                    continue
                dst[dst_x, dst_y] = min(dst[a_x, a_y], dst[b_x, b_y]) + (max(dst[a_x, a_y], dst[b_x, b_y]) - min(dst[a_x, a_y], dst[b_x, b_y])) * (dst_y - a_y) / magni

    return dst


def bicubic_interpolation(src, dst_shape):
    pass


def lagrange_interpolation(src, dst_shape):
    pass
