from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
img_bulb = Image.open('./Pokedex/bulbasaur.jpg')
img_char = Image.open('./Pokedex/charmander.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SMOOTH)
filtered_img3 = img.filter(ImageFilter.SHARPEN)
filtered_img4 = img.convert('L')

filtered_img.save("blur.png", 'png')

filtered_img2.save("smooth.png",'png')

filtered_img3.save("sharpen.png",'png')

filtered_img4.save('gray.png','png')


img_bulb.show() # it should open it in a new tab

rotated_img = filtered_img4.rotate(90)
rotated_img.save('rotated.png','png')

resized_img = img_bulb.resize((300,300))
resized_img.save('resized.png','png')

box = (100,100,200,200)
cropped_img = img_char.crop(box)
cropped_img.save('cropped.png','png')

print(img.mode)
print(img.format)
print(img.size)


