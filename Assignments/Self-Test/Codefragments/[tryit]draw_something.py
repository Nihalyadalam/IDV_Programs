from PIL import Image, ImageDraw, ImageFont
from simshow import simshow

IMAGE_WIDTH =                   #define the image width
IMAGE_HEIGHT =                  #define the image height

image = Image.new("RGB", (IMAGE_WIDTH, IMAGE_HEIGHT))
draw = ImageDraw.Draw(image)

print("image width: ", image.size[0])
print("image height: ", image.size[1])

draw.line((0, 0) + image.size, fill=128)
draw.line((0, image.size[1], image.size[0], 0))
draw.rectangle( ((image.size[0]/2, image.size[1]/2), (image.size[0], image.size[1])), fill="blue")
draw.rectangle( ((image.size[0]/2, image.size[1]/2), (image.size[0]/3, image.size[1]/3)), fill="green")

text_position = ( , )  # define the position of the following text
draw.text(text_position, "Hello!")

image.save("draw_something.png")
simshow("draw_something.png")
