import os, sys, shutil

'''=============================== variable ==============================='''
ext_list = ['avi','mp4','mkv','mpg','wmv','flv','mov']
first_path = "./"
dst = "./destination"
'''=============================== code ==============================='''

ext_stack = []
f = open("./filename.txt","w")
#print(f_list)

for(path, dir, files) in os.walk(first_path):
    for filename in files:
        f_ext = os.path.splitext(filename)[-1]
        for ext in ext_list:
            print(f_ext,f_ext == '.'+ext,ext)
            if f_ext == '.'+ext or f_ext == '.'+ext.upper():
                f.write(filename+'\n')
        ext_stack.append(f_ext+'\n')
        

f.close()