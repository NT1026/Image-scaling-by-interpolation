import argparse
import cv2
import enlarge_method

method_help = """
Enlarge method: 
Use Nearest-Neighbor please set value as 1.
Use Bilinear Interpolation please set value as 2.
Use Bicubic Interpolation please set value as 3.
Use Lagrange Interpolation please set value as 4.
"""

method = {
    1: enlarge_method.nearest_neighbor,
    2: enlarge_method.bilinear_interpolation,
    3: enlarge_method.bicubic_interpolation,
    4: enlarge_method.lagrange_interpolation
}

mode = {
    "GRAY": 1,
    "RGB": 3
}


if __name__ == "__main__":
    # Parameter settings
    parser = argparse.ArgumentParser()
    configs = parser.add_argument_group(title="configurations")
    configs.add_argument("--enlarge", help="Enlarge magnitude.", type=int)
    configs.add_argument("--image", help="Path of your image.")
    configs.add_argument("--method", help=method_help, type=int)
    configs.add_argument("--mode", help="GRAY or RGB")
    args = parser.parse_args()

    # Parse parameter
    _magni = args.enlarge
    _img_path = args.image
    _method = args.method
    _mode = args.mode

    # Result
    if _mode == "GRAY":
        src = cv2.imread(_img_path, cv2.IMREAD_GRAYSCALE)
    else:
        src = cv2.imread(_img_path)

    dst_height = src.shape[0] * _magni
    dst_width = src.shape[1] * _magni
    channels = mode[_mode]
    dst = method[_method](src, dst_shape=(dst_height, dst_width, channels))

    # Output
    cv2.namedWindow('src', cv2.WINDOW_NORMAL) 
    cv2.resizeWindow('src', src.shape[1], src.shape[0])
    cv2.imshow("src",src) 

    cv2.namedWindow('dst', cv2.WINDOW_NORMAL) 
    cv2.resizeWindow('dst', dst.shape[1], dst.shape[0])
    cv2.imshow("dst",dst)

    # Press any key to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
