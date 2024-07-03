from PIL import Image, ImageDraw
import os

#Loads the image through the console
route = input("Ingresa la ruta de la imagen: ") 
while (not os.path.exists(route)):
    route = input("Ruta no existe. Ingresa la ruta de la imagen: ")

os.chdir("\\".join(route.split("\\")[0:-1])) #Changes the current directory to the directory where the image is.
img = Image.open(route.split("\\")[-1]) #Select the image in the direcory.

step = 5 #Sets the size of the pixel.
draw = ImageDraw.Draw(img) #Loads the image on the canvas.

#Goes trough a set of pixels determined by the step variable,
#Setting the color of the pixel of the middle as the color of the set.
for y in range(0, img.size[1], step):
    for x in range(0, img.size[0], step):
        if img.format == "PNG":
            (r,g,b,a) = img.getpixel((x + int(step/2), y + int(step/2)))
        else:
            (r,g,b) = img.getpixel((x + step/2, y + step/2))
        draw.rectangle((x, y, x + step, y + step), fill=(r, g, b))

#Saves the image in the "ImagenesFiltradas" directory.
if not os.path.exists("ImagenesFiltradas"):
    os.makedirs("ImagenesFiltradas")
os.chdir("ImagenesFiltradas")
img.save(f"{img.filename.split("\\")[-1].split(".")[0]}Pixelator.{(img.format).lower()}")