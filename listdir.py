import os #import operating system library
img_path = ('<absolute-path-here>') #define path to directory

#load filenames into array
file_list = []
for f in os.scandir(img_path):
    file_list.append(f.name)

#print array of file names
for i in (0, len(file_list)):
    print(file_list)
