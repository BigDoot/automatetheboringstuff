#!python3
#!extending chapter project

from PIL import Image
import os

squarefitsize = 300
logofilename = 'catlogo.png'

logoim = Image.open(logofilename)
logowidth, logoheight = logoim.size

os.makedirs('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 17\\withlogo', exist_ok=True)
for filename in os.listdir('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 17'):
    if not filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp') or filename == logofilename:
        continue
    im = Image.open(filename)
    imwidth, imheight = im.size
    if imwidth > squarefitsize and imheight > squarefitsize:
        print('Resizing %s' %filename)
        if imwidth > imheight:
            im = im.resize((squarefitsize, int(imheight*squarefitsize/imwidth)))
        else:
            im = im.resize((int(imwidth*squarefitsize/imheight), squarefitsize))
    if not im.size[0] > 2*logowidth and im.size[1] > 2*logoheight:
        continue
    im.paste(logoim, ((im.size[0]-logowidth),(im.size[1]-logoheight)), logoim)
    print('Adding logo to %s' %filename)
    im.save(os.path.join('C:\\Users\\glend\\OneDrive\\Desktop\\python stuff\\chapter 17\\withlogo', filename))
