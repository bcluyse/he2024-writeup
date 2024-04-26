import math
import numpy as np

import cv2

# Load an image using cv2.imread()
image_path = './average_cropped.png'  # Change 'image.jpg' to the path of your image file
image = cv2.imread(image_path)
gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(np.float64)

x_blocks = 40
x_length = len(image[0])
y_blocks = 55
y_length = len(image)

x_step = x_length / x_blocks
y_step = y_length / y_blocks

mask = [[0 for x in range(0, x_blocks)] for y in range(0, y_blocks)]
total_white = [[0 for x in range(0, x_blocks)] for y in range(0, y_blocks)]


for i in range(0, y_length):
    for j in range(0, x_length):
        i_block = math.floor(i / y_step)
        j_block = math.floor(j / x_step)
        block = gray_frame[i, j]
        if block > 250:
            total_white[i_block][j_block] += 1


for i in range(len(mask)):
    for j in range(len(mask[0])):
        if total_white[i][j] > 3:
            mask[i][j] = 1


pangram = "1028456432waltzb_dnymph{for}quickj?gsvex"
flag = ""
for i in range(y_blocks):
    for j in range(x_blocks):
        if mask[i][j] == 1:
            print(i, j)
            idx = j % len(pangram)
            flag += (pangram[idx])

print(flag, len(flag))
