import numpy as np


def nearest_neighbor(src, dst_shape):
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

    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            # Find the corresponding coordinates
            src_x = int(dst_x * (src_width / dst_width))
            src_y = int(dst_y * (src_height / dst_height))
            
            # Interpolation
            if channels == 1:
                dst[dst_x, dst_y] = src[src_x, src_y]

            if channels == 3:
                dst[dst_x, dst_y, :] = src[src_x, src_y, :]

    return dst


def bilinear_interpolation():
    pass


def bicubic_interpolation():
    pass


def lagrange_interpolation():
    pass
