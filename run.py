import subprocess

"""
Enlarge mode: 
Use Nearest-Neighbor please set value as 1.
Use Bilinear Interpolation please set value as 2.
Use Bicubic Interpolation please set value as 3.
Use Lagrange Interpolation please set value as 4.
"""

magni = 3
img_path = "images/img.png"
method = 2
mode = "GRAY"

if __name__ == "__main__":
    subprocess.run(["python3", "main.py", "--enlarge", str(magni), "--image", img_path, "--method", str(method), "--mode", mode])
