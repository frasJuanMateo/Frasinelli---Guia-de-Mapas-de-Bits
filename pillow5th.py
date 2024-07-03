from PIL import Image
import os

#Ask for the routes of the image and watermark, and doesn't let you through if the image is smaller than the watermark.
while True:
    routeImg = input("Ingresa la ruta de la imagen: ")
    while (not os.path.exists(routeImg)):
        routeImg = input("Ruta no existe. Ingresa la ruta de la imagen: ")
    os.chdir("\\".join(routeImg.split("\\")[0:-1]))
    img = Image.open(routeImg.split("\\")[-1])

    routeWM = input("Ingresa la ruta de la marca de agua: ")
    while (not os.path.exists(routeWM)):
        routeWM = input("Ruta no existe. Ingresa la ruta de la marca de agua: ")
    os.chdir("\\".join(routeWM.split("\\")[0:-1]))
    wtrMrk = Image.open(routeWM.split("\\")[-1])

    if (wtrMrk.size[0] + 100 <= img.size[0] and wtrMrk.size[1] + 100 <= img.size[1]):
        break
    print("La marca de agua es muy grande.")

#Ask the user 4 options to paste the image and doesn't let you through if the answer is not valid.
wtrMrk = wtrMrk.copy()
while True:
    option = (input("En que esquina se pondra la marca de agua? Superior izquierda [1], Superior derecha [2], Inferior izquierda [3] o Inferior derecha [4]: "))

    if option == "1":
        img.paste(wtrMrk, (50, 50))
        break
    if option == "2":
        img.paste(wtrMrk, (img.size[0] - wtrMrk.size[0] - 50, 50))
        break
    if option == "3":
        img.paste(wtrMrk, (50, img.size[1] - wtrMrk.size[1] - 50))
        break
    if option == "4":
        img.paste(wtrMrk, (img.size[0] - wtrMrk.size[0] - 50, img.size[1] - wtrMrk.size[1] - 50))
        break
    print("Opcion invalida.")

#Saves the image.
img.save(f"{img.filename.split("\\")[-1].split(".")[0]} waterMarked.{img.format}")