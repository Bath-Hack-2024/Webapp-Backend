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
                return [width,height, max_value]

def track_star(images):
    # Load the first image
    first_image = Image.open(images[0]).convert('L')

    # Find the position of the brightest star in the first image
    [width1, height1, max_value] = find_brightest_star(first_image)
    allDiffs = [0] * (len(images)-1)
    # Track the star in the subsequent images
    for i in range(1, len(images)):
        # Load the current image
        current_image = Image.open(images[i]).convert('L')

        nowBrightness = current_image.getpixel((width1, height1))

        diffBright = nowBrightness - max_value

        # Print the distance between the positions
        print(f"Difference in brightness: {diffBright}")
        allDiffs[i-1] = diffBright
    
    maxDiff = max(allDiffs)
    ratio = maxDiff / max_value
    return ratio


# List of image file paths
image_files = ["src/levelTwo/testData/image1.png", "src/levelTwo/testData/image2.png", "src/levelTwo/testData/image3.png"]

# Call the track_star function with the list of image files
ratio = track_star(image_files)

print(ratio)
