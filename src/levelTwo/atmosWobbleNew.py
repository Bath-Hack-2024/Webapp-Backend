from PIL import Image
import numpy
import argparse

# Function to find the atmospheric wobble
# Uses the variance of the brightest star in the first image
# Then compares the variance of the same place in subsequent images
# Returns the maximum difference in variance

def find_brightest_star(image):
    # Takes a greyscale image
    # Finds the brightest pixel in the image and gets its value
    region_of_interest = image.crop((5, 5, image.size[0]-5, image.size[1]-5))
    max_value = numpy.amax(region_of_interest)
    variances = []

    # Iterates through the image to find the coordinates of the brightest pixel
    for width in range(5, image.size[0]-5):
        for height in range(5, image.size[1]-5):
            if image.getpixel((width, height)) == max_value:
                # Takes the variance of the 3x3 square around the brightest pixel
                for x in numpy.arange(width-3, width+4):
                    for y in numpy.arange(height-3, height+4):
                        variances.append(image.getpixel((x, y)))

                var_total = numpy.var(variances)
                # Returns the coordinates of the brightest pixel and the variance of the 3x3 square around it
                return [width, height, var_total]

def track_star(images):
    # Loads the first image as a greyscale image
    first_image = Image.open(images[0]).convert('L')
    variances = []
    # Find the position of the brightest star in the first image and its variance
    [width1, height1, max_value] = find_brightest_star(first_image)
    all_diffs = [0] * (len(images)-1)
    # Iterate through the rest of the images
    for i in range(1, len(images)):
        # Load the current image as a greyscale image
        current_image = Image.open(images[i]).convert('L')
        # Finds the variance of a 3x3 square around the coordinates of the brightest pixel in the first image
        for x in numpy.arange(width1-3, width1+4):
            for y in numpy.arange(height1-3, height1+4):
                variances.append(current_image.getpixel((x, y)))

        var_bright = numpy.var(variances)
        # Find the difference in variance between the first image and the current image
        diff_bright = var_bright - max_value
        all_diffs[i-1] = diff_bright
    
    # Returns the maximum difference in variance between the first image and the rest of the images
    max_diff = max(numpy.absolute(all_diffs))
    return max_diff

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the maximum difference in variance of the brightest star between the first image and the rest of the images.')
    parser.add_argument('images', type=list, nargs='+', help='List of image file paths')
    args = parser.parse_args()

    max_diff_variance = track_star(args.images)
    print("Max difference in variance:", max_diff_variance)
