
import cv2
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import numpy as np
from rembg import remove
import easyocr
path = ('input_vid2.mp4')
cap = cv2.VideoCapture(path)
print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
ret, frame = cap.read()
img = cv2.imread('sample_frame3.png')

bg_rem = remove(img)


def find_largest_rectangle(binary_image):
    # Convert binary image to single-channel format (grayscale)
    _, binary_image = cv2.threshold(binary_image, 140, 255, cv2.THRESH_BINARY)
    binary_image = cv2.cvtColor(binary_image, cv2.COLOR_BGR2GRAY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize variables to store the largest rectangle
    largest_area = 0
    largest_rectangle = None

    # Iterate through the contours
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Find the area of the polygon
        area = cv2.contourArea(approx)

        # Check if the area is the largest so far
        if area > largest_area:
            largest_area = area
            largest_rectangle = approx

    return largest_rectangle

# Assuming 'r' is the binary image obtained from the thresholding operation
# (Make sure 'r' is a binary image, e.g., after cv2.threshold)

# Find the largest rectangle
largest_rectangle = find_largest_rectangle(bg_rem)

# Draw the largest rectangle on a copy of the original image
image_with_largest_rectangle = img.copy()
cv2.drawContours(image_with_largest_rectangle, [largest_rectangle], -1, (0, 255, 0), 2)

# Get the bounding box of the largest rectangle
x, y, w, h = cv2.boundingRect(largest_rectangle)

# Crop the image to the bounding box of the largest rectangle
cropped_image = img[y:y+h, x:x+w]

# Convert BGR to RGB before displaying with plt.imshow
cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
reader = easyocr.Reader(['en'])
res = reader.readtext(cropped_image)
import cv2
import matplotlib.pyplot as plt

#

# Display the cropped image
plt.imshow(cropped_image_rgb)
plt.show()
fig, ax = plt.subplots(figsize=(8, 5))
data = res

ax.set_xlim(0, 1600)
ax.set_ylim(900, 0)


for rect_data, label, _ in data:
    rect = patches.Polygon(rect_data, closed=True, edgecolor='r', facecolor='none')
    ax.add_patch(rect)


    center_x = (rect_data[0][0] + rect_data[2][0]) / 2
    center_y = (rect_data[0][1] + rect_data[2][1]) / 2

    ax.text(center_x, center_y, label, color='b', ha='center', va='center')


plt.show()
for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    if frame_idx % 32 == 0:
        bg_rem = remove(frame)
        largest_rectangle = find_largest_rectangle(bg_rem)

        # Draw the largest rectangle on a copy of the original image
        image_with_largest_rectangle = img.copy()
        cv2.drawContours(image_with_largest_rectangle, [largest_rectangle], -1, (0, 255, 0), 2)

        # Get the bounding box of the largest rectangle
        x, y, w, h = cv2.boundingRect(largest_rectangle)

        # Crop the image to the bounding box of the largest rectangle
        cropped_image = img[y:y + h, x:x + w]

        # Convert BGR to RGB before displaying with plt.imshow
        cropped_image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
        reader = easyocr.Reader(['en'])
        res = reader.readtext(bg_rem)
        plt.imshow(bg_rem)
        plt.show()
        fig, ax = plt.subplots(figsize=(8, 5))
        data = res
        read_vals = [string for string in res]
        print(read_vals)
        ax.set_xlim(0, 1400)
        ax.set_ylim(800, 0)

        for rect_data, label, _ in data:
            rect = patches.Polygon(rect_data, closed=True, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

            center_x = (rect_data[0][0] + rect_data[2][0]) / 2
            center_y = (rect_data[0][1] + rect_data[2][1]) / 2

            ax.text(center_x, center_y, label, color='b', ha='center', va='center')

        cv2.imshow("Frames", frame)
        cv2.waitKey(0)  # wait for a keyboard input


cv2.destroyAllWindows()