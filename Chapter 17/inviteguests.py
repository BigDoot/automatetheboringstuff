#!python3
#pretty simplistic, no flower image unfortunately, or fonts or fontsize
#if you really wanted to do this irl there are probably better programs
#to download cos its not worth the trouble doing it with a python script..

import os
from PIL import Image, ImageDraw, ImageColor

file = open('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 17\\guests.txt')
guests = file.read()
guestslist = guests.split('\n')
#flowerim = Image.open('')

for guests in guestslist:
    im = Image.new('RGBA', (288,360), 'purple')
    draw = ImageDraw.Draw(im)
    draw.rectangle((0,0,287,359))
    draw.text((10,90), 'IT WOULD BE THE PLEASURE TO HAVE THE COMPANY OF', fill='black')
    draw.text((120, 120), guests, fill='black')
    draw.text((50,160), 'AT 11010 MEMORY LANE ON THE EVENING OF', fill='black')
    draw.text((130, 200), 'APRIL 1ST', fill='black')
    im.save(os.path.join('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 17\\guests', '%sinvitation.png'%guests))
