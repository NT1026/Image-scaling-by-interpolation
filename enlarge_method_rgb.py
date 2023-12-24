import numpy as np


def nearest_neighbor(src_img, dst_shape, magni):
    src = np.pad(src_img, ((0, 1), (0, 1), (0, 0)), mode="reflect")
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
            
            dst[dst_x, dst_y, :] = src[src_x, src_y, :]

    return dst


def bilinear_interpolation(src_img, dst_shape, magni):
    src = np.pad(src_img, ((0, 1), (0, 1), (0, 0)), mode="reflect")
    dst_height, dst_width, channels = dst_shape[0], dst_shape[1], dst_shape[2]
    dst = np.zeros(shape=(dst_height, dst_width, channels), dtype=np.uint8)

   # Interpolation
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            x, y = dst_x / magni, dst_y / magni
            src_x, src_y = int(x), int(y)

            dst[dst_x, dst_y, :] = (src_x + 1 - x) * (src_y + 1 - y) * src[src_x    , src_y    , :] + \
                                   (x - src_x)     * (src_y + 1 - y) * src[src_x    , src_y + 1, :] + \
                                   (src_x + 1 - x) * (y - src_y)     * src[src_x + 1, src_y    , :] + \
                                   (x - src_x)     * (y - src_y)     * src[src_x + 1, src_y + 1, :]
            
    return dst


def W(_x):
    a = -0.5
    x = abs(_x)
    if x <= 1:
        return (a + 2) * (x ** 3) - (a + 3) * (x ** 2) + 1
    elif x < 2:
        return a * (x ** 3) - 5 * a * (x ** 2) + 8 * a * x - 4 * a
    else:
        return 0
    

def bicubic_matmul(src, src_x, src_y, u, v):
    A = np.array([W(u + 1), W(u), W(u - 1), W(u - 2)])
    A = A[np.newaxis, :]

    B = src[src_x: src_x + 4, src_y: src_y + 4]

    C = np.array([W(v + 1), W(v), W(v - 1), W(v - 2)])
    C = C[:, np.newaxis]

    dst = np.zeros(3, dtype=np.float32)
    for i in range(3):
        tmp = np.matmul(np.matmul(A, B[:, :, i]), C)
        if tmp > 255:
            dst[i] = 255
        elif tmp < 0:
            dst[i] = 0
        else:
            dst[i] = tmp
    
    return dst


def bicubic_interpolation(src_img, dst_shape, magni):
    src = np.pad(src_img, ((1, 2), (1, 2), (0, 0)), mode="reflect")
    dst_height, dst_width, channels = dst_shape[0], dst_shape[1], dst_shape[2]
    dst = np.zeros(shape=(dst_height, dst_width, channels), dtype=np.uint8)

    # Interpolation
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            x, y = dst_x / magni, dst_y / magni
            src_x, src_y = int(x), int(y)
            u, v = x - src_x, y - src_y
            dst[dst_x, dst_y, :] = bicubic_matmul(src, src_x, src_y, u, v)

    return dst


def lagrange_interpolation(src, dst_shape):
    pass
