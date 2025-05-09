import os
import shutil
import sys
import time
sys.set_int_max_str_digits(0)

multiplefolders=False

zipsize = input("input the size of the zip: ") #12GB
zipname = input("enter zip name: ")

start = time.time()

specifiedformat = []
zipsizeinspecifiedformat = []

for i in zipsize:
    if i.isnumeric():
        zipsizeinspecifiedformat.append(i)
    else:
        specifiedformat.append(i)

specifiedformat = [j for j in specifiedformat if j != " "]

Format = ""
for l in specifiedformat:
    Format = Format+l
size = ""
for k in zipsizeinspecifiedformat:
    size = size+k

if Format == "kb":
    multiplefolders = False
    size = int(size)*1024
elif Format == "mb":
    multiplefolders = False
    size = int(size)*1048576
elif Format == "gb":
    multiplefolders = True
    folderamount = int(size)
    size = int(size)*1073741824

if multiplefolders:
    index = 0
    os.mkdir(os.path.join(os.path.join(os.getcwd(), "files"), zipname))

    for i in range(folderamount):
        index+=1
        os.mkdir(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+str(index)))

        index1 = 0
        for j in range(10):
            index1+=1
            file = open(os.path.join(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+str(index), zipname+str(index1))), "x")

            file.write("0"*int(size/folderamount/10))
            file.close()

        shutil.make_archive(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+str(index)), "zip", os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+str(index)))

        index1 = 0
        for j in range(10):
            index1+=1
            os.remove(os.path.join(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+str(index), zipname+str(index1))))

    index = 0
    for i in range(folderamount):
        index+=1
        os.rmdir(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+str(index)))

    shutil.copy(os.path.join(os.getcwd(), "unzip.py"), os.path.join(os.path.join(os.getcwd(), "files"), zipname))

    shutil.make_archive(os.path.join(os.path.join(os.getcwd(), "files"), zipname), "zip", os.path.join(os.path.join(os.getcwd(), "files"), zipname))

else:
    os.mkdir(os.path.join(os.path.join(os.getcwd(), "files"), zipname))

    file = open(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+".txt"), "x")
    file.write("0"*int(size))
    file.close()

    shutil.make_archive(os.path.join(os.path.join(os.getcwd(), "files"), zipname), "zip", os.path.join(os.getcwd(), "files"), zipname)
    os.remove(os.path.join(os.path.join(os.path.join(os.getcwd(), "files"), zipname), zipname+".txt"))
    os.rmdir(os.path.join(os.path.join(os.getcwd(), "files"), zipname))

end = time.time()
time = end-start
print("that took "+str(round(time,1))+" seconds")
