#! python3
#Import modules and write comments to describe this program.
import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('C:\\'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.lower().endswith('.png') or filename.lower().endswith('.jpg'):
            numNonPhotoFiles += 1
            print(filename + ' is not a photo.')
            continue    # skip to next filename

        # Open image file using Pillow.
        try:
            im = Image.open(filename)
        except:
            continue
        width, height = im.size

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
            print(filename + ' is a photo!')
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1
            print(filename + 'is not a photo.')

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print(os.path.abspath(foldername))
