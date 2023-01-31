import os
import cv2


path = "PRO-C105-Project-Images-main"

images = []


for file in os.listdir(path):
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)
output = cv2.VideoWriter("sunset2.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,size)
for i in range(91,0,-1):
    frame = cv2.imread(images[i])
    output.write(frame)