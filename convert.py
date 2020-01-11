#Converte Colour Photo Into Black & White

from PIL import Image

open_image = Image.open("photo.jpg")
convert_to_bw = open_image.convert("L")
convert_to_bw.show()
convert_to_bw.save("photo_bw.jpg")