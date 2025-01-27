import requests
from PIL import Image
from io import BytesIO

r = requests.get("https://images.unsplash.com/photo-1449034446853-66c86144b0ad?w=620&auto=format&fit=crop&q=60&ixlib=rb-4.0.3") # replace with your image url
i = Image.open(BytesIO(r.content)) # open the image file
fp = open("img.jpg", "wb") # open the image file in binary write mode
i.save(fp) # save the image to the file
fp.close() # close the file