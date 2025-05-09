import os
import shutil

filelist = os.listdir(os.getcwd())

filelist.remove("unzip.py")

for i in range(len(filelist)):
    os.mkdir(os.path.join(os.getcwd(), filelist[i].removesuffix(".zip")))
    shutil.unpack_archive(os.path.join(os.getcwd(), filelist[i]), os.path.join(os.getcwd(), filelist[i].removesuffix(".zip")), "zip")
