from PIL import Image
import os

o = 10 #Amount of the blurring

def sum(valMtrx): #Function to get the average of the colors of the pixels
    res = [0, 0, 0]
    for value in range(3):
        sum = 0
        count = 0
        for j in range(len(valMtrx)):
            for i in range(len(valMtrx[j])):
                if valMtrx[j][i] != None:
                    sum += valMtrx[j][i][value]
                    count += 1
        res[value] = round(sum / count)
    
    return tuple(res)

def getValMtrx(x, y, o): #Function to pass
    mtrx = []
    for j in range(o):
        arr = []
        for i in range(o):
           
            mtrxX = x + (i - int(o/2))
            mtrxY = y + (j - int(o/2))

            if mtrxX < 0 or mtrxY < 0 or mtrxX > img.size[0] - 1 or mtrxY > img.size[1] - 1:
                arr.append(None)
            
            else:
                arr.append(img.getpixel((mtrxX, mtrxY)))

        mtrx.append(arr)
    
    return mtrx

route = input("Ingresa la ruta de la imagen: ")
while (not os.path.exists(route)):
    route = input("Ruta no existe. Ingresa la ruta de la imagen: ")
os.chdir("\\".join(route.split("\\")[0:-1]))
img = Image.open(route.split("\\")[-1])

#Gets the average of the set around one of the pixels and then sets that average as the color of that pixel.
for y in range(img.size[1]):
    for x in range(img.size[0]):
        img.putpixel((x, y), (sum(getValMtrx(x, y, o))))

#Saves the image in the "ImagenesFiltradas" directory.
if not os.path.exists("ImagenesFiltradas"):
    os.makedirs("ImagenesFiltradas")
os.chdir("ImagenesFiltradas")
img.save(f"{img.filename.split("\\")[-1].split(".")[0]}Gaussian.{(img.format).lower()}")

