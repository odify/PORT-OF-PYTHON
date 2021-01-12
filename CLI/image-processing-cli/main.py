#!/usr/bin/env python3


from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageFilter,ImageOps
import PIL


#import a picture and rename it to 'image.jpg'

img = PIL.Image.open('image.jpg')


image_file = img.convert('1')
#or import multiple images

#edit the script for your optional processing

image_file.save('b+w.png')

converter = PIL.ImageEnhance.Brightness(img).enhance(4.5)
converter.save('brightness.jpg')

converter = PIL.ImageEnhance.Color(img).enhance(4.5)
converter.save('colorful.jpg')

blur = img.filter(ImageFilter.GaussianBlur(radius = 10)) 
blur.save('blur.jpg') 


converter = PIL.ImageEnhance.Contrast(img).enhance(4.5)
converter.save('highcontrast.jpg')


im = ImageOps.posterize(img, 3)  
im.save('posterized.jpg')


inverted_image = PIL.ImageOps.invert(img)
inverted_image.save('invert.png')


crop = img.crop((0, 0, 2500, 2500))
crop.save('cropped.jpg')


rotate = img.rotate(180)
rotate.save('rotated.jpg')


im_mirror = ImageOps.mirror(img)
im_mirror.save('mirror.jpg')


height,width = img.size
image_data = img.load()
for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = image_data[loop1,loop2]
        image_data[loop1,loop2] = 0,g,0
img.save('changecolor.jpeg')


#draw = ImageDraw.Draw(img)
#font = ImageFont.truetype('arial.ttf', size=80)
#draw.text((50, 50), 'hello world',fill = 'rgb(0, 0, 0)', font=font)
#img.save('draw.jpg')




til = Image.open('pin.png')
img.paste(til,(00,10))
img.save('paste.jpg')





img.save("compress.jpg",optimize=True,quality=10)
