from PIL import Image
 
img = Image.new('L', (10, 20), color = (125))
img.save('pil_gray.png')

img = Image.new('L', (10, 20), color = (255))
img.save('pil_white.png')

img = Image.new('RGB', (10, 20), color = 'green')
img.save('pil_green.png')

img = Image.new('RGB', (10, 20), color = (10, 20, 255))
img.save('pil_blue.png')

#######################################
#fill image pixel by pixel

width = 10
height = 20
img = Image.new("L", (width, height))
pixelMap = img.load()

for y in range(height):
	for x in range(width):
		pixelMap[x,y] = x*y*2
img.save('pil_gray_shine.png')


#######################################
#draw a line

img = Image.new('RGBA', (width, height), color = (255, 255, 255))
pixelMap = img.load()
rangeValue = height
for n in range(rangeValue):
    x = 5
    y = n
    pixelMap[x, y] = (0, 0, 255, n*10)
img.save('pil_line_vertical.png')


#######################################
#draw a horizontal line in red at the top of the image

img = Image.new('RGB', (width, height), color = (0, 0, 0))
pixelMap = img.load()
rangeValue =                                    #define range value
for n in range(rangeValue):
    x =                                         #define x
    y =                                         #define y
    pixelMap[x, y] =                            #define red color
img.save('pil_line_horizontal.png')