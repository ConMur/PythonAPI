import requests
import shutil
import random

from PIL import Image

width = random.randint(1, 1000)
height = random.randint(1,1000) 

url = "http://placekitten.com/" + str(width) + "/" + str(height)

response = requests.get(url, stream = True)

image = Image.open(response.raw)

image.show()

del response
