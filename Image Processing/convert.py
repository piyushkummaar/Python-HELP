'''
JPG to PNG Converter
'''

import os 
import sys
from PIL import Image
import glob
import random 

input_folder = sys.argv[1]
output_folder = sys.argv[2]
files = glob.glob(input_folder+"*jpg")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in files:    
    img = Image.open(i)
    img.save(output_folder+"/"+"new"+str(random.randint(0, 10))+".png")
