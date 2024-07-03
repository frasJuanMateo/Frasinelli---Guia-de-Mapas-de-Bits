from PIL import Image
import os
from tabulate import tabulate

route = input("Ingresa la ruta de la imagen: ") #Gets the image directory through the console.

#The route gets divided in 2. The image directory route and the filename of the image.
os.chdir("\\".join(route.split("\\")[0:-1])) #Changes the current directory to the directory where the image is.
img = Image.open(route.split("\\")[-1]) #Select the image in the direcory.

img.show() #Opens the image file.

imgData = [[img.filename.split("\\")[-1].split(".")[0], img.format, f"{img.size[0]} x {img.size[1]}", str(img.size[0] * img.size[1]), img.filename]]
#Saves the image data and then prints it as a table with tabulate.
print(tabulate(imgData, headers=["Nombre", "Extensión", "Resolución", "Cantidad de píxeles", "Ruta"]))