import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the image
img = cv2.imread(r"D:\Lexicon_Labs\Deep_Learning\Day_1\image.jpg", cv2.IMREAD_COLOR)  # Make sure file name matches exactly

# Check if the image loaded correctly
if img is None:
    print("Error: Image not found or cannot be loaded.")
    exit()

# Print the image shape
print("Image shape:", img.shape)  # (height, width, channels)

# Questions:
# The three values in shape represent: (height, width, channels)
# height -> number of rows
# width -> number of columns
# channels -> number of color channels (BGR)
# Data type of image array
print("Image data type:", img.dtype)  # usually uint8

# 2. Access and modify a single pixel
# Access pixel at (y=50, x=100) (row=50, col=100)
pixel = img[50, 100]
print("Original pixel value at (50,100):", pixel)

# OpenCV stores color as BGR
# Modify pixel to red (B=0, G=0, R=255)
img[50, 100] = [0, 0, 255]

# 3. Display the updated image using OpenCV
cv2.imshow("Updated Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Questions:
# In OpenCV, colors are stored in BGR order
# Setting all values to maximum [255,255,255] -> white pixel
# Setting all values to zero [0,0,0] -> black pixel

# 4. Modify a region of the image
# Example: change a 100x100 rectangle starting at (50,50)
img[50:150, 50:150] = [0, 255, 0]  # green rectangle

cv2.imshow("Modified Region", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Questions:
# Slicing in NumPy: img[start_row:end_row, start_col:end_col]
# Row range -> vertical (height)
# Column range -> horizontal (width)
# All channels are modified unless specified