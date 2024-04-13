from PIL import Image
import numpy

#Function to find the atmospheric wobble
#Uses the varience of the brightest star in the first image
#Then compares the the varience of the same place in subsequent images
#Returns the maximum difference in varience

def find_brightest_star(image):

    #Takes a greyscale image
    #Finds the brightest pixel in the image and gets the value of it
    max_value = numpy.amax(image)
    varience = []

    #Iterates through the image to find the coordinates of the brightest pixel
    for width in range(image.size[0]):
        for height in range(image.size[1]):
            if image.getpixel((width, height)) == max_value:
                #Takes the varience of the 3x3 square around the brightest pixel
                for x in numpy.arange(width-3,width+4):
                    for y in numpy.arange(height-3,height+4):
                        varience.append(image.getpixel((x, y)))

                varTotal = numpy.var(varience)
                #Returns the coordinates of the brightest pixel and the varience of the 3x3 square around it
                return [width,height, varTotal]

def track_star(images):
    #Loads the first image as a greyscale image
    first_image = Image.open(images[0]).convert('L')
    varience = []
    #Find the position of the brightest star in the first image and its varience
    [width1, height1, max_value] = find_brightest_star(first_image)
    allDiffs = [0] * (len(images)-1)
    #Iterate through the rest of the images
    for i in range(1, len(images)):
        #Load the current image as a greyscale image
        current_image = Image.open(images[i]).convert('L')
        #Finds the varience of a 3x3 square around the coordinates of the brightest pixel in the first image
        for x in numpy.arange(width1-3,width1+4):
            for y in numpy.arange(height1-3,height1+4):
                varience.append(current_image.getpixel((x, y)))

        varBright = numpy.var(varience)
        #Find the difference in varience between the first image and the current image
        diffBright = varBright - max_value
        allDiffs[i-1] = diffBright
    
    #Returns the maximum difference in varience between the first image and the rest of the images
    maxDiff = max(numpy.absolute(allDiffs))
    return maxDiff

#INPUTS:
#List of image files
maxDiffVarience = track_star(image_files)
#OUTPUTS:
#Maximum difference in varience of the brightest star between the first image and the rest of the images
