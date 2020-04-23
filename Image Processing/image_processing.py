from PIL import Image, ImageFilter


img = Image.open("profil.jpg")
print(img.format, img.size, img.mode)
# new_img = img.resize((400,400))
#new_img = img.thumbnail((300, 300))
#img.save("thumnail.jpg")
# filter_img = img.filter(ImageFilter.BLUR)
# filter_img.save("blug.png","png")
convert_img = img.convert('L')
convert_img.save("profil.png")
# convert_img.show()
