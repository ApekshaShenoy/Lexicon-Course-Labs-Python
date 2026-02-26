import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Lexicon_Labs\Deep_Learning\Day_1\image.jpg", cv2.IMREAD_COLOR)  

#checking  if the image was loaded successfully
if img is None:
    print("Error: Image not found or cannot be loaded.")
    exit()
    
print("Image shape:", img.shape)  # (height, width, channels)

# Questions:
# The three values in shape represent: (height, width, channels)
# height -> number of rows
# width -> number of columns
# channels -> number of color channels (BGR)

print("Image data type:", img.dtype)  

# Access pixel at (y=50, x=100) (row=50, col=100)
pixel = img[50, 100]
print("Original pixel value at (50,100):", pixel)

img[50, 100] = [0., 0, 255]
cv2.imshow("Updated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Questions:
# In OpenCV, colors are stored in BGR order
# Setting all values to maximum [255,255,255] -> white pixel
# Setting all values to zero [0,0,0] -> black pixel

img[50:150, 50:150] = [0, 255, 0]  # green 

cv2.imshow("Modified Region", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Questions:
# Slicing in NumPy: img[start_row:end_row, start_col:end_col]
# Row range is vertical (height)
# Column range  is horizontal (width)
# All channels are modified unless specified