from PIL import Image
rdim = (249,380)
Which_file = str(input('Enter the location of the image(Make sure the aspect ratio of the file is close to 2x3): '))
baseimage = Image.open(Which_file)
in_img = Image.open('iamge2.jpg')
width, height = in_img.size
print(width)
print(height)
ratio = (rdim[0]/rdim[1])

if abs((width/height)-(ratio))>=0.025:
    if ((height*ratio)>width):
        print('Your image is too tall')
        image_cut = height - ((width)*(1/ratio))
        percentcut = image_cut*100/height
        whichcrop = str(input('Which part of image do you want to stay? (top/bottom/middle): '))
        if whichcrop == 'bottom':
            image_final = in_img.crop((0, image_cut, width, height))
        elif whichcrop == 'top':
            image_final = in_img.crop((0, 0, width, height - image_cut))
        elif whichcrop =='middle':
            image_final = in_img.crop((0,(image_cut/2),width ,height-(image_cut/2)))
    if ((width*(1/ratio)))>height:
        print('Your image is too wide')
        image_cut = width - ((height*ratio))
        percentcut = image_cut*100/width
        whichcrop = str(input('Which part of image do you want to stay? (left/right/middle): '))
        if whichcrop == 'left':
            image_final = in_img.crop((0, 0,width - image_cut, height))
        elif whichcrop == 'right':
            image_final = in_img.crop((image_cut, 0, width, height))
        elif whichcrop == 'middle':
            image_final = in_img.crop((image_cut/2, 0, width - (image_cut / 2), height))
        else:
            print('enter a valid answer')

newin_img = image_final.resize(rdim)
baseimage.paste(newin_img,(46,78))
baseimage.save('Output.png')
