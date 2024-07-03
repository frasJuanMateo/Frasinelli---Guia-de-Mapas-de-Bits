from PIL import Image
import os

#Loads the image through the console
route = input("Ingresa la ruta de la imagen: ") 
while (not os.path.exists(route)):
    route = input("Ruta no existe. Ingresa la ruta de la imagen: ")
    
os.chdir("\\".join(route.split("\\")[0:-1])) #Changes the current directory to the directory where the image is.
img = Image.open(route.split("\\")[-1]) #Select the image in the direcory.

WBLimit = 58 #Sets the limit beetween black and white (The lower the value, the darker)

#Goes through all the pixels, getting their brightness
#And setting them to Black or White, depending on their value.
for y in range(img.size[1]):
    for x in range(img.size[0]):
        (r,g,b) = img.getpixel((x, y))
        if (r + g + b) / 3 > WBLimit:
            img.putpixel((x, y), (255, 255, 255))
        else:
            img.putpixel((x, y), (0, 0, 0))

#Saves the image in the "ImagenesFiltradas" directory.
if not os.path.exists("ImagenesFiltradas"):
    os.makedirs("ImagenesFiltradas")
os.chdir("ImagenesFiltradas")
img.save(f"{img.filename.split("\\")[-1].split(".")[0]}BN.{(img.format).lower()}")