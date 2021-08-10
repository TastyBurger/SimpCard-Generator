from PIL import Image
rdim = (249,380)
Which_file = str(input('Enter the location of the image(Make sure the aspect ratio of the file is close to 2x3): '))
baseimage = Image.open('bfile.png')
in_img = Image.open(Which_file)
newin_img = in_img.resize(rdim)
baseimage.paste(newin_img,(46,78))
baseimage.save('Output.png')
