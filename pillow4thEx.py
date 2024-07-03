from PIL import Image
import os

#Asks the image route through the console and doesn't let you continue unless you enter a valid directory.
route = input("Ingresa la ruta de la imagen: ")
while (not os.path.exists(route)):
    route = input("Ruta no existe. Ingresa la ruta de la imagen: ")

os.chdir("\\".join(route.split("\\")[0:-1])) #Changes the current directory to the directory where the image is.
img = Image.open(route.split("\\")[-1]) #Select the image in the direcory.
imgFormat = img.format.lower() #Saves the image format in a variable.

#Asks the first coordinate of the crop through the console and doesn't let you continue unless you enter a valid directory.
firstCord = (int(input("Ingrese la coordenada x inicial para empezar el corte: ")), int(input("Ingrese la coordenada y inicial para empezar el corte: ")))
while (firstCord[0] >= img.size[0] or firstCord[1] >= img.size[1] or firstCord[0] < 0 or firstCord[1] < 0):
    firstCord = (int(input("Valor no valido. Ingrese la coordenada x inicial para empezar el corte: ")), int(input("Valor no valido. Ingrese la coordenada y inicial para empezar el corte: ")))
img = img.crop((firstCord[0], firstCord[1], img.size[0], img.size[1]))

#Asks the size of the crop through the console and doesn't let you continue unless you enter a valid directory.
cutSize = (int(input("Ingrese el valor del ancho del corte: ")), int(input("Ingrese el valor del alto del corte: ")))
while (cutSize[0] > img.size[0] or cutSize[1] > img.size[1] or cutSize[0] <= 0 or cutSize[1] <= 0):
    cutSize = (int(input("Valor no valido. Ingrese el valor del ancho del corte: ")), int(input("Valor no valido. Ingrese el valor del alto del corte: ")))

img = img.crop((0, 0, cutSize[0], cutSize[1])) #Sets the image as its crop.

#Creates (if not already created) the image crops directory, shows the crop and then saves it in the new directory.
if not os.path.exists("recortes"):
    os.mkdir("recortes")
os.chdir("recortes")
i = 1
while os.path.exists(f"recorte{i}.{imgFormat}"):
    i += 1
img.show()
img.save(f"recorte{i}.{imgFormat}")