import sys
from PIL import Image, ImageDraw, ImageFont

droppedFile = sys.argv[1]
#the dragging method, printing droppedFile will get it's path which is all we need


def save_image(image, path):
  image.save(path, 'png')
#i know there are other methods but it is what it is

def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


def get_pixel(image, i, j):
  #going Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None
  pixel = image.getpixel((i, j))
  return pixel
def convert_primary(image):
  # Getting the size
  width, height = image.size

  # Creating new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()
  
  # Transforming to primary
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)
      
      # RGB palette
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Where all the magic happens
      if red > 127:
        red = 255
      else:
        red = 0
      if green > 127:
        green = 255
      else:
        green = 0
      if blue > 127:
        blue = 255
      else:
        blue = 0

      # and voila
      pixels[i, j] = (int(red), int(green), int(blue))

  # results =
  return new

try:
  image = Image.open(droppedFile)
  #opening the image 
  
  fontType = ImageFont.truetype('impact.ttf',100)
  fontType2 = ImageFont.truetype('impact.ttf',103)
  #explained down
  draw = ImageDraw.Draw(image)
  width,height = image.size
  
  newWidth = ((width/2)-(width/7))
  newHeight = (height-(height/5))-10
  #this is smart (y), just so it goes in the middle
  
  draw.text(xy=(newWidth,newHeight),text="NIGGA",fill=(255,0,0),font=fontType2)
  draw.text(xy=(newWidth,newHeight),text="NIGGA",fill=(255,255,255),font=fontType)
  #since distortion makes text hard to read i made two fonts for two words, it's like shadow but not really, see in results
  #sorry for the racist words, but you came here for memes not to be get offended
  
  new = convert_primary(image)
  #activating the magic
  save_image(new, "cringe.png")
  #voila
except Exception as e:
  print(e)
  #because the file is PYW you won't see any error but if nothing comes out, change PYW to PY in the file name 
  #and add an input() so you'll see the error

  
