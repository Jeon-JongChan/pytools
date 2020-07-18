import os, sys, shutil

'''=============================== variable ==============================='''
ext_list = ['avi','mp4','mkv','mpg','wmv','flv','mov']
first_path = "./"
dst_path = "./destination/"

'''=============================== code ==============================='''

ext_stack = []
#f = open("./filename.txt",'w+')

if not os.path.exists(dst_path):
    os.makedirs(dst_path)
    
for(path, dir, files) in os.walk(first_path):
    for filename in files:
        f_ext = os.path.splitext(filename)[-1]
        for ext in ext_list:
            if f_ext == '.'+ext or f_ext == '.'+ext.upper():
                file_path = path+'/'+filename
                size = os.path.getsize(file_path)
                mb_size = size / (1024.0 * 1024.0) #MB
                if mb_size < 100:
                    print(file_path + " is not movie. byte : ",size)
                    continue
                if os.path.exists(dst_path+filename): # file 존재시
                        print(file_path+" is existed, move. destination : ", dst_path,filename+"_1")
                        shutil.move(file_path, dst_path+filename+"_1")
                        continue
                print(file_path+" is move. destination : ", dst_path)
                shutil.move(file_path, dst_path)
                #f.write(path+'/'+filename+'\n')
        ext_stack.append(f_ext+'\n')

#f.close()