import subprocess

"""
Enlarge mode: 
Use Nearest-Neighbor please set value as 1.
Use Bilinear Interpolation please set value as 2.
Use Bicubic Interpolation please set value as 3.
Use Lagrange Interpolation please set value as 4.
"""

imgs = {
    1: "images/100x100.jpg",
    2: "images/316x316.jpg",
    3: "images/600x600.jpg",
    4: "images/1600x1200.jpg"
}

magni = 8
img_path = imgs[1]
method = 1
mode = "RGB"

if __name__ == "__main__":
    subprocess.run(["python3", "main.py", "--enlarge", str(magni), "--image", img_path, "--method", str(method), "--mode", mode])
