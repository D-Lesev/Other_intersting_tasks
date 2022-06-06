import numpy as np
from PIL import Image

width, height = 600, 800

#creating the image
img = np.zeros((height, width, 3), dtype=np.uint8)

#creating the back color
img[:] = (35, 29, 43)

# creating the floor color
img[int(height*0.85):height] = (35, 55, 43)

# creating building
img[int(height*0.1):int(height*0.9), int(width*0.1):int(width*0.9)] = (94, 101, 107)

# Creating windows
for row in range(6):
    for column in range(5):
        if np.random.randint(0,8) == 5: #choose every time random windows
            window_color = (240, 230, 140)
        else:
            window_color = (28, 23, 35)
        img[
        int(height*0.1 + 100*row + 20):int(height*0.1 + 100*row + 60 + 20),
        int(width*0.2 + 75*column + 15):int(width*0.2+ 75*column +30 + 15)
        ] = window_color

#Saving image
Image.fromarray(img).save("my_second_img.png")