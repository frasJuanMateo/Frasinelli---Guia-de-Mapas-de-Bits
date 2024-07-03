from PIL import Image
import os

route = input("Ingresa la ruta de la imagen: ") #Gets the image directory through the console.

#The route gets divided in 2. The image directory route and the filename of the image.
os.chdir("\\".join(route.split("\\")[0:-1])) #Changes the current directory to the directory where the image is.
img = Image.open(route.split("\\")[-1]) #Select the image in the direcory.

rotation = int(input("Ingrese la cantidad de grados que quiere rotar la imagen: ")) #Gets the rotation of the image through the console.

img.rotate(rotation).show() #Shows the image rotated.
img.rotate(rotation).save(f"{img.filename.split("\\")[-1].split(".")[0]}{rotation}.{img.format}") #Saves the rotated image.