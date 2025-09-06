import shutil
#shutil.rmtree("new_directory")

# Copy a file
shutil.copy("Day-9/read.txt", "Day-10/my_file_copy.txt")
 
# Move a file or directory
shutil.move("Day-10/my_file_copy.txt", "new_directory/")



#Use os when you need simple path/directory management.

#Use shutil when you need to copy, move, delete whole directories, or archive files.