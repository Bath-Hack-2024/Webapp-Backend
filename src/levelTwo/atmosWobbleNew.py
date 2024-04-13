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
    varience = []
    #print(max_value)
    for width in range(gray.size[0]):
        for height in range(gray.size[1]):
            if gray.getpixel((width, height)) == max_value:
                print(numpy.arange(width-3,width+4))
                for x in numpy.arange(width-3,width+4):
                    for y in numpy.arange(height-3,height+4):
                        varience.append(gray.getpixel((x, y)))

                varTotal = numpy.var(varience)
                print(varTotal)
                return [width,height, varTotal]

def track_star(images):
    # Load the first image
    first_image = Image.open(images[0]).convert('L')
    varience = []
    # Find the position of the brightest star in the first image
    [width1, height1, max_value] = find_brightest_star(first_image)
    allDiffs = [0] * (len(images)-1)
    # Track the star in the subsequent images
    for i in range(1, len(images)):
        # Load the current image
        current_image = Image.open(images[i]).convert('L')

        for x in numpy.arange(width1-3,width1+4):
            for y in numpy.arange(height1-3,height1+4):
                varience.append(current_image.getpixel((x, y)))

        varBright = numpy.var(varience)

        diffBright = varBright - max_value

        # Print the distance between the positions
        print(f"Difference in varience: {diffBright}")
        allDiffs[i-1] = diffBright
    
    maxDiff = max(numpy.absolute(allDiffs))
    return maxDiff


# List of image file paths
image_files = ["src/levelTwo/testData/image1.png", "src/levelTwo/testData/image2.png", "src/levelTwo/testData/image3.png"]

# Call the track_star function with the list of image files
ratio = track_star(image_files)

print(ratio)
