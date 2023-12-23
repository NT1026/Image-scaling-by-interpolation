import numpy as np


def larger(a, b):
    max = a if a >= b else b
    return max


def smaller(a, b):
    min = a if a < b else b
    return min


def nearest_neighbor(src, dst_shape, magni):
    # Original image size
    src_height = src.shape[0]
    src_width = src.shape[1]
    
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
            src_x = int(dst_x * (src_width / dst_width))
            src_y = int(dst_y * (src_height / dst_height))
            
            dst[dst_x, dst_y] = src[src_x, src_y]

    return dst


def bilinear_interpolation(src, dst_shape, magni):
    # Original image size
    src_height = src.shape[0]
    src_width = src.shape[1]

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
            elif int(dst_x / magni) == dst_x / magni:
                (a_x, a_y) = (int(dst_x / magni), int(dst_y / magni))
                (b_x, b_y) = (int(dst_x / magni), int(dst_y / magni) + 1)
                if b_x > src_height - 1 or b_y > src_width - 1:
                    continue
                dst[dst_x, dst_y] = smaller(src[a_x, a_y], src[b_x, b_y]) + (larger(src[a_x, a_y], src[b_x, b_y]) - smaller(src[a_x, a_y], src[b_x, b_y])) * (dst_y - a_y * magni) / magni
            elif int(dst_y / magni) == dst_y / magni:
                (a_x, a_y) = (int(dst_x / magni), int(dst_y / magni))
                (b_x, b_y) = (int(dst_x / magni) + 1, int(dst_y / magni))
                if b_x > src_height - 1 or b_y > src_width - 1:
                    continue
                dst[dst_x, dst_y] = smaller(src[a_x, a_y], src[b_x, b_y]) + (larger(src[a_x, a_y], src[b_x, b_y]) - smaller(src[a_x, a_y], src[b_x, b_y])) * (dst_x - a_x * magni) / magni

    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            if (int(dst_x / magni) != dst_x / magni) and (int(dst_y / magni) != dst_y / magni):
                (a_x, a_y) = (dst_x, int(dst_y / magni) * magni)
                (b_x, b_y) = (dst_x, int(dst_y / magni) * magni + magni)
                if b_x > dst_height - 1 or b_y > dst_width - 1:
                    continue
                dst[dst_x, dst_y] = smaller(dst[a_x, a_y], dst[b_x, b_y]) + (larger(dst[a_x, a_y], dst[b_x, b_y]) - smaller(dst[a_x, a_y], dst[b_x, b_y])) * (dst_y - a_y) / magni

    return dst


def bicubic_interpolation(src, dst_shape):
    pass


def lagrange_interpolation(src, dst_shape):
    pass
