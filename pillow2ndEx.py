from PIL import Image
import os

route = input("Ingresa la ruta de la imagen: ") #Gets the image directory through the console.

#The route gets divided in 2. The image directory route and the filename of the image.
os.chdir("\\".join(route.split("\\")[0:-1])) #Changes the current directory to the directory where the image is.
img = Image.open(route.split("\\")[-1]) #Select the image in the direcory.

img.show() #Opens the image file.
img.copy() #Copies the image.

imgCopy = Image.new(img.mode, img.size) #Creates a new image
imgCopy.paste(img) #Pastes the old image in the new one.
imgCopy.save(f"Copia_de_{route.split("\\")[-1]}") #Saves the new image.