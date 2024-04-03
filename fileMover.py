# This script will move any files inside the downloads folder (~/Downloads) with certain prefixes into certain folders for quick file organization. 
# Not only will it move the file(s) to the correct folder, but it will remove the prefix so that the name looks normal once organized.
# For instance, 
# b_ = backgrounds, so it gets moved to the backgrounds folder at ~/Desktop/OtherStuff/Backgrounds
# pfp_ = profile pictures
# d_ = desktop

# Automatic mode:
# The files already have prefixes and will be moved to the proper folders automatically

# Manual mode:
# The files will be sorted through one-by-one and moved to folders numerically (1=desktop, 1.3=desktop/Otherstuff, 1.3.3=Desktop/OtherStuff/Backgrounds, etc)
# If there are nested folders, the user will sort the file numerically

import os
import shutil
downloadPath = '/home/grimm/Downloads/'
desktopPath  = '/home/grimm/Desktop/'

def clearScreen():
    os.system('clear')

def moveFile(dest, file):
    source = downloadPath + file
    newDest = dest + file
    shutil.move(source, newDest)

runConfirm = input("Run FileMover?[Y/n] ")

if runConfirm.lower() == 'y' and len(os.listdir(downloadPath)) == 0:
    print("Downloads folder appears to be empty, no point in trying to clear an empty folder!")
    
elif runConfirm.lower() == 'y' and len(os.listdir(downloadPath)) != 0:
    clearScreen()
    # os.chdir(downloadPath)    
    files = os.listdir(downloadPath)
    
    print("Download folder contents: ")
    for fileName in files:
        print("\t", fileName)
    
    modeConfirm = input("\nList modes, run manual mode, or automatic mode?[l/a/m] ")
    if modeConfirm.lower() == 'l':
        print("\nAutomatic Mode: sorts the files based on the file extension")
        print("Manual Mode: sort each file one-by-one with folders denoted by numbers")
        print("")
    
    elif modeConfirm.lower() == 'a':
        clearScreen()
        print("Automatic mode chosen, starting now!")
        # For each file in the /home/grimm/Downloads folder
        for file in files:
            # If the file is longer than 5 chars, stops from getting ab.cd scenarios
            if len(file) > 5:
                
                # Sorting downloaded 3d print files                
                if file.endswith(".stl", len(file)-4):
                    dest = desktopPath + "3dPrinterStuff/Downloaded/"
                    moveFile(dest, file)
                    print("Moved to the 3d prints folder:\t", file)
                
                # Sorting downloaded images
                elif os.path.splitext(file)[1] in (".jpeg", ".webp", ".jpg", ".png", ".gif"):
                    # Other ways of doing that ^^^
                    # elif any(file.endswith(extension) for extension in [".jpeg", ".webp", ".jpg", ".png", ".gif"]):
                    # elif file.endswith(".jpeg", len(file)-5) or file.endswith(".webp", len(file)-5) or file.endswith(".jpg", len(file)-4) or file.endswith(".png", len(file)-4):  
                    dest = desktopPath + "OtherStuff/Images/"
                    moveFile(dest, file)
                    print("Moved to the photos folder:\t", file)
                    
                # If the filetype is not one of the above
                else:   
                    dest = desktopPath + "OtherStuff/Misc/"
                    moveFile(dest, file)
                    print("Moved to the misc folder:\t", file)

            
        print("\nAll done!")
        
        
    elif modeConfirm.lower() == 'm':
        clearScreen()
        print("Manual mode chosen, starting now!")
        
        for file in files: 
            os.chdir('/home/grimm/')
            dirCount = 1
            response = ""
            
            while response != '0':
                print("You are currently at", os.getcwd())
                print("Moving file", file, "to: ")
                print(".         Move file to cwd")
                print("..        Back")
                print("0         Exit/Skip file")
                
                # allDirs = os.listdir(os.getcwd())
                allDirs = [newDir for newDir in os.listdir(os.getcwd()) if not newDir.startswith('.') and os.path.isdir(newDir)]
                for dir in allDirs:
                    print(dirCount, "\t ", dir)
                    dirCount += 1
                
                response = input("Where go? ")
                if response == '.':
                    dest = os.getcwd() + "/"
                    moveFile(dest, file)
                    # print("Moved", file, "to", os.getcwd())
                    clearScreen()
                    break
                elif response == '..' and os.getcwd() != "/home/grimm":
                    os.chdir(response)
                    clearScreen()
                elif response.isnumeric() and int(response) > 0 and int(response) <= dirCount-1:
                    os.chdir(allDirs[int(response)-1])
                
                clearScreen()
                dirCount = 1
        
        print("Thats was the last file. Ending manual mode!")
        
    # End cases
    else:
        clearScreen()
else:
    clearScreen()
    
# clearScreen()
