import cv2
from PIL import Image
import numpy
import math

def find_brightest_star(image):
    # Convert image to grayscale
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = image
    # Find the brightest spot in the image
    #_, max_val, _, max_loc = cv2.minMaxLoc(gray)
    max_value = numpy.amax(gray)
    print(gray.size)
    #print(max_value)
    for width in range(gray.size[0]):
        for height in range(gray.size[1]):
            if gray.getpixel((width, height)) == max_value:
                return [width,height]

def track_star(images):
    # Load the first image
    first_image = Image.open(images[0]).convert('L')

    # Find the position of the brightest star in the first image
    [width1, height1] = find_brightest_star(first_image)

    # Track the star in the subsequent images
    for i in range(1, len(images)):
        # Load the current image
        current_image = Image.open(images[i]).convert('L')

        # Find the position of the brightest star in the current image
        [width, height] = find_brightest_star(current_image)

        # Calculate the distance between the current and previous positions
        distance = math.hypot(width - width1, height - height1)

        # Print the distance between the positions
        print(f"Distance between image {i} and image {i-1}: {distance}")

        # Update the star position for the next iteration
        #star_position = current_star_position

# List of image file paths
image_files = ["src/levelTwo/testData/image1.png", "src/levelTwo/testData/image2.png", "src/levelTwo/testData/image3.png"]

# Call the track_star function with the list of image files
track_star(image_files)