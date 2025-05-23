import cv2
import os

theme = "pwnachu"
scale = 2

faces = []
source_faces_path = f"./custom-themes/{theme}/faces_{theme}"
dest_faces_path = f"./custom-themes/{theme}/faces_{theme}-resized"

for file in os.listdir(source_faces_path):
    if file.endswith(".png"):
        faces.append(file)

os.mkdir(dest_faces_path, exist_ok=True)

for face in faces:
    img = cv2.imread(f"{source_faces_path}/{face}", cv2.IMREAD_GRAYSCALE)
    im_bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    img_resized = cv2.resize(im_bw, (img.shape[1] * scale, img.shape[0] * scale))
    im_resized_bw = cv2.threshold(img_resized, 127, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(f"{dest_faces_path}/{face}", im_resized_bw)