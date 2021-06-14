''' This tool to convert from 4 channel images to 3 channel images'''

from PIL import Image

  
# Creating a image object, of the sample image
img = Image.open(r'#000.png')
  
# A 12-value tuple which is a transform matrix for dropping 
# green channel (in this case)

  
# Transforming the image to RGB using the aforementioned matrix 
img = img.convert("RGB")
  
# Displaying the image 
img.show()
img.save('#new1.png')