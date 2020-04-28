#i !/usr/bin/env python3

import sys
import os
import glob
import re

#python3 rm.py ./file ./test ./foldee ./haha -r

# initialized
listFile = sys.argv[1:]
recurse = False
trash_path = "~/rm_trash" 
dic = {}
trash_path = os.path.expanduser(trash_path)
existList = glob.glob(trash_path + "/*.*")

# check if the arg inputs valid
if len(sys.argv) <= 0:
    print("Invalid File Path Input:")
    sys.exit(1)

# check if trash dir exists
if not os.path.isdir(trash_path):
    os.mkdir(trash_path)

# check for recurse
if "-r" in listFile:
    recurse = True
    while "-r" in listFile:
        listFile.remove("-r")
    
#add existing files in the trash into the dictionaries
for exist in existList:
    exist2 = re.sub(r"./rm_trash/*","",exist)
    dic[exist2] = 0

# go thru all input files from args
for fFile in listFile:
   
    #check if exists ################## CAN DO IT BETTER for condition
    if not os.path.isfile(fFile) and not os.path.isdir(fFile):
        sys.stderr.write("rm.py: cannot remove'" + os.path.basename(fFile) + "': No such file or directory \n")
        continue
    
    #check if it is a dir and if we have to recursively delete it
    if os.path.isdir(fFile) and not recurse:
        sys.stderr.write("rm.py: cannot remove '" + os.path.basename(fFile) + "': Is a directory \n")
        continue
    
    #extra local variable incase name of destination change: distribution
    fFile2 = fFile

    #extract name from path
    exist2 = os.path.basename(fFile)   
    
    #check for duplicate, else add to dictionary
    if exist2 in dic:
        dic[exist2] += 1
        newDup = os.path.splitext(fFile)

        #if there is file extension: ex .txt
        if newDup[1]:
            fFile2 = newDup[0] + '-' + str(dic[exist2]) + newDup[1]
        else:
            fFile2 = newDup[0] + newDup[1] + '-' + str(dic[exist2])
    else:
        dic[exist2] = 0
    
    # new path name 
    newPath = trash_path + "/" + os.path.basename(fFile2)
    
    #copy and remove file/dir
    os.system('cp -r {0} {1}'.format(fFile,newPath))
    os.system('rm -r {0}'.format(fFile)) 
