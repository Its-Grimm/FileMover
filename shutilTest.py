import os 
import shutil

fileName = "buster-sword-pagemark.stl"
downloadsFolder = "/home/grimm/Downloads/" 
destinationFolder = "/home/grimm/Desktop/3dPrinterStuff/Downloaded/"

# data[0] prints out only the file name, data[1] prints out only the file extension 
# data = os.path.splitext(fileName2)
# print(data[0])
# print(data[1])

# /home/grimm/Downloads/buster-sword-pagemark.stl
source = downloadsFolder + fileName
destination = destinationFolder + fileName

shutil.move(source, destination)
print("Moved", fileName, "to", destinationFolder)





