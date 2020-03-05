from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img4 = img.convert('L')

filtered_img.save("blur.png", 'png')

filtered_img2.save("smooth.png",'png')

filtered_img3.save("sharpen.png",'png')

filtered_img4.save('gray.png','png')

print(img.mode)
print(img.format)
print(img.size)

