# Imports
import os
import shutil

# Variables
src = (r"C:\Users\anton\OneDrive\Skrivbord\Pictures")
newSrc = (r"D:\Foto\Backup")
src_files = os.listdir(src)
counter = 0

print('Starting backup of files')

# Loop the directory and only copy files which are not already in the back up and are pictures
for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        full_new_file_name = os.path.join(newSrc, file_name)
        if not os.path.isfile(full_new_file_name):
            if full_file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                shutil.copy(full_file_name, newSrc)
                counter = counter+1

print('Number of files: ' + str(counter))
print('Files copied to backup!')
