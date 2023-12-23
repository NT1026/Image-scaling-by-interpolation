import argparse
import cv2
import enlarge_method_gray
import enlarge_method_rgb

method_help = """
Enlarge method: 
Use Nearest-Neighbor please set value as 1.
Use Bilinear Interpolation please set value as 2.
Use Bicubic Interpolation please set value as 3.
Use Lagrange Interpolation please set value as 4.
"""

method = {
    1: enlarge_method_gray.nearest_neighbor,
    2: enlarge_method_gray.bilinear_interpolation,
    3: enlarge_method_gray.bicubic_interpolation,
    4: enlarge_method_gray.lagrange_interpolation,
    5: enlarge_method_rgb.nearest_neighbor,
    6: enlarge_method_rgb.bilinear_interpolation,
    7: enlarge_method_rgb.bicubic_interpolation,
    8: enlarge_method_rgb.lagrange_interpolation
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
        dst = method[_method](src, dst_shape=(src.shape[0] * _magni, src.shape[1] * _magni, mode[_mode]), magni=_magni)

    elif _mode == "RGB":
        src = cv2.imread(_img_path)
        dst = method[_method + 4](src, dst_shape=(src.shape[0] * _magni, src.shape[1] * _magni, mode[_mode]), magni=_magni)


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
