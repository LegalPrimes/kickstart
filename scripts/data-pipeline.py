import os #import operating system library
import json
from darknetpy.detector import Detector
img_path = ('/FilepathHere/') #define path to directory

#load filenames into array
file_list = []
for f in os.scandir(img_path):
    file_list.append(f.name)

#create index
index = '/FilepathHere/index.txt'
jsonfile = open('/FilepathHere/blob.json', 'a+')
filenum = 0
if os.path.isfile(index):
    filename = open(index, 'r')
    if filename:
        filenum = filename.read()
        filename.close()
#darknetpy
detector = Detector('/FilepathHere/darknet',
                    '/FilepathHere/darknet/cfg/coco.data',
                    '/FilepathHere/darknet/cfg/yolov2.cfg',
                    '/FilepathHere/darknet/yolov2.weights')

#Define array to hold results
results = {}

#JSON
output = {}
output['ImageID'] = ''
output['YOLOOutputString'] = results
for i in range(int(filenum), len(file_list) - 1):
    results[i] = detector.detect(img_path + file_list[i])
    output['ImageID'] = file_list[i]
    output['YOLOOutputString'] = results[i]
    json_blob = json.dumps (output)
    print (file_list[i] + ' ###COMPLETE###' + '\n' )
    print (i, file=open('/FilepathHere/index.txt', 'w'))
    jsonfile.write(json_blob +'\n')
print(results)
#print (json.loads(stdout_json)['ImageID'])
