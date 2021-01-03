import os, sys, shutil
from datetime import datetime

target_log = "./qbittorrent.log"
target_path = "./20210103/"
dst_path = "./"
dst_path += datetime.today().strftime("%Y%m%d") + "_chk/"


def chk_file(target_log, target_path, dst_path):
    f = open(target_log,'r',encoding='UTF-8')
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
        
    lines = f.readlines()

    for line in lines:
        fsplit = line.split("'")
        if len(fsplit) < 2:
            print("################################# 로그메세지가 다릅니다.")
            break
        fname = line.split("'")[1]
        fname += ".torrent"
        
        if os.path.exists(target_path+fname):
            print(fname+" 파일 존재. 파일을 이동시킵니다.")
            shutil.move(target_path+fname, dst_path+fname)

    f.close()

try:
    chk_file(target_log, target_path, dst_path)
except Exception as e:
    print("예외발생",e)



os.system("pause")