import os, sys, shutil
import cv2 

'''=============================== variable ==============================='''
ext_list = ['avi','mp4','mkv','mpg','wmv','flv','mov']
first_path = "./"
dst_path = "./destination/"
except_dir = ["destination","except","notEncode"]
limit = [854,480]
'''=============================== code ===============================''' 

ext_stack = [] 

def isFolder(path):
    if not os.path.exists(path):
        os.makedirs(path)
isFolder(dst_path) 

def getVideoInfo(file_path):
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened() :
        print(file_path+" is not there")
        return None
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    return [width,height] 

def checkResolution(vinfo, file_path):
    if(vinfo[0] <= limit[0] and vinfo[1] <= limit[1]):
        isFolder(dst_path+"notEncode/")
        print("> > > "+file_path+" is Moved. satisfied resolution")
        shutil.move(file_path, dst_path+"notEncode/")
    elif(vinfo[0] <= limit[0] or vinfo[1] <= limit[1]):
        isFolder(dst_path+"except/")
        print("> > > "+file_path+" is Moved. one resolution is satisfied")
        shutil.move(file_path, dst_path+"except/")
    else:
        print("> > > "+file_path+" is not Move. not satisfied resolution")

for(path, dir, files) in os.walk(first_path):
    if path.split('/')[-1] in except_dir: 
        print("============ except dir : ", path,"==============")
        continue
    for filename in files:
        f_ext = os.path.splitext(filename)[-1]
        for ext in ext_list:
            if f_ext == '.'+ext or f_ext == '.'+ext.upper():
                file_path = path+'/'+filename
                info = getVideoInfo(file_path)
                checkResolution(info, file_path)
        ext_stack.append(f_ext+'\n')
#f.close() 


