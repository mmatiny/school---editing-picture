from PIL import Image

#These defs most of them had been written in the past except mirror_top_bottom and mirror_left_right
#The new defs had been written by Mohammad Matin
#And he had been collected and correct some def into correct format 
def grayscale(img): 
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            n=int((r+b+g)/3)
            img.putpixel((x, y), (n, n, n))
    return img

def colour_edit(img):
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            n=(r+g+b)/3
            if n>127.5:
                n=255
            else:
                n=0
            img.putpixel((x, y), (n, n, n))
    return img

def negative(img):
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            r = 255-r ; g = 255-g ; b = 255-b
            img.putpixel((x, y), (r, b, g))
    return img

def rotated(img,x):
    while True:
        img=img.rotate(x)
        return img

def detail(img):

    x=("Format: {0}\nSize: {1}\nMode: {2}".format(img.format,img.size, img.mode))

    return x

def blur(img):
    img = img.filter(ImageFilter.BLUR)
    
    return img

def flip_left_right(img1):
    width = img1.size[0]
    height = img1.size[1]
    img2=img1.copy()
    for i in range(width):
        for j in range(height):
            r,g,b = img1.getpixel((width-i-1, j))
            img2.putpixel((i,j),(r,g,b))
            
    return img2

def flip_top_bottom(img1):
    width = img1.size[0]
    height = img1.size[1]
    img2=img1.copy()
    for i in range(width):
        for j in range(height):
            r,g,b = img1.getpixel((i, height-j-1))
            img2.putpixel((i,j),(r,g,b))
            
    return img2

def mirror_right_left(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((width-i-1, j))
            img.putpixel((i,j),(r,g,b))
            
    return img

def mirror_left_right(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(width-1,-1,-1):
        for j in range(height):
            r,g,b = img.getpixel((width-i-1, j))
            img.putpixel((i,j),(r,g,b))
            
    return img

def mirror_bottom_top(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(width):
        for j in range(height):
            r,g,b = img.getpixel((i, height-j-1))
            img.putpixel((i,j),(r,g,b))
            
    return img

def mirror_top_bottom(img):
    width = img.size[0]
    height = img.size[1]
    for i in range(width):
        for j in range(height-1,-1,-1):
            r,g,b = img.getpixel((i, height-j-1))
            img.putpixel((i,j),(r,g,b))
            
    return img

def blueinstaaa (img):
    
    y=0
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            ny=int(g+b+50)
            nye=ny
            img.putpixel((x, y), (nye-255, nye-255,nye-0))
    
    return img
    
def redinstaa (img):
    
    y=0
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            ny=int(g+b+50)
            nye=ny
            img.putpixel((x, y), (nye-0, nye-255,nye-255))
    
    return img
def greeninstaa (img):
     
    y=0
    weight = img.size[0]
    height = img.size[1]
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            ny=int(g+b+50)
            nye=ny
            img.putpixel((x, y), (nye-255, nye-0,nye-255))
     
    return img
