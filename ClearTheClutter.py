# write a program to clear the clutter inside the folder on your computer.
# You should use OS module to rename all png images from  1.txt all the way till n.txt where n is the total number of png images in the folder.
# do the same for other file formats.

import os
def clutter(folder_path):
    i=1
    for filename in os.listdir(folder_path):
        name,ext=os.path.splitext(filename)
        if ext==".txt":
            newname=str(i)+ext
            old_path=os.path.join(folder_path,filename)
            new_path=os.path.join(folder_path,newname)
            os.rename(old_path,new_path)
            i+=1


folder_path = "C:/Users/Lenovo/OneDrive/Desktop/temporary"
clutter(folder_path)
