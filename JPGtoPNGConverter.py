import sys 
import os 

from PIL import Image 

# use sys module, grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)
#check if folder exists , if not, create it 

if not os.path.exists(output_folder):
  os.makedirs(output_folder)

#loop through the entire folder and then convert to .png
for filename in os.listdir(image_folder):
  img = Image.open(f'{image_folder}{filename}')
  clean_name = os.path.splitext(filename)
  print(clean_name)

  img.save(f'{output_folder}{filename}','png')
  print('all done!')
  
#save them to the new folder 
