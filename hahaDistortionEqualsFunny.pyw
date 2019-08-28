import sys
droppedFile = sys.argv[1]


from PIL import Image, ImageDraw, ImageFont
def save_image(image, path):
  image.save(path, 'png')

def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None
  pixel = image.getpixel((i, j))
  return pixel
def convert_primary(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()
  
  # Transform to primary
  for i in range(width):
    for j in range(height):
      # Get Pixel
      pixel = get_pixel(image, i, j)
      
      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to primary
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

      # Set Pixel in new image
      pixels[i, j] = (int(red), int(green), int(blue))

  # Return new image
  return new

try:
  image = Image.open(droppedFile)
  fontType = ImageFont.truetype('impact.ttf',100)
  fontType2 = ImageFont.truetype('impact.ttf',103)
  draw = ImageDraw.Draw(image)
  
  width,height = image.size
  newWidth = ((width/2)-(width/7))
  newHeight = (height-(height/5))-10
  
  draw.text(xy=(newWidth,newHeight),text="NIGGA",fill=(255,0,0),font=fontType2)
  draw.text(xy=(newWidth,newHeight),text="NIGGA",fill=(255,255,255),font=fontType)
  new = convert_primary(image)
  save_image(new, "cringe.png")
except Exception as e:
  print(e)

  
