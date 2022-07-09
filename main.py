import os
 
# Get the list of all files and directories
path = "C://test//"
dir_list = os.listdir(path)

print(dir_list)

for item in dir_list:    
    os.rename(path + item, path + item.replace(" ", "_"));
    
