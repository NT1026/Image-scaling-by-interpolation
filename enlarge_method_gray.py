import numpy as np


def nearest_neighbor(src_img, dst_shape, magni):  
    src = np.pad(src_img, ((0, 1),(0, 1)), mode="reflect")
    dst_height, dst_width, channels = dst_shape[0], dst_shape[1], dst_shape[2]
    dst = np.zeros(shape=(dst_height, dst_width, channels), dtype=np.uint8)

    # Interpolation
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            x, y = dst_x / magni, dst_y / magni
            src_x, src_y = int(x), int(y)

            if x - src_x >= 0.5:
                src_x += 1
            if y - src_y >= 0.5:
                src_y += 1
            
            dst[dst_x, dst_y] = src[src_x, src_y]

    return dst


def bilinear_interpolation(src_img, dst_shape, magni):
    src = np.pad(src_img, ((0, 1),(0, 1)), mode="reflect")
    dst_height, dst_width, channels = dst_shape[0], dst_shape[1], dst_shape[2]
    dst = np.zeros(shape=(dst_height, dst_width, channels), dtype=np.uint8)

    # Interpolation
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            x, y = dst_x / magni, dst_y / magni
            src_x, src_y = int(x), int(y)

            dst[dst_x, dst_y] = (src_x + 1 - x) * (src_y + 1 - y) * src[src_x    , src_y    ] + \
                                (x - src_x)     * (src_y + 1 - y) * src[src_x    , src_y + 1] + \
                                (src_x + 1 - x) * (y - src_y)     * src[src_x + 1, src_y    ] + \
                                (x - src_x)     * (y - src_y)     * src[src_x + 1, src_y + 1]
    
    return dst


def bicubic_interpolation(src, dst_shape):
    pass


def lagrange_interpolation(src, dst_shape):
    pass
