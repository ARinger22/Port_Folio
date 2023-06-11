from rembg import remove
from PIL import Image
  
# Store path of the image in the variable input_path
input_path =  'WhatsApp Image 2023-06-05 at 11.12.53 AM.jpeg'
  
# Store path of the output image in the variable output_path
output_path = 'gfgoutput.png'
  
# Processing the image
input = Image.open(input_path)
  
# Removing the background from the given Image
output = remove(input)
  
#Saving the image in the given path
output.save(output_path)