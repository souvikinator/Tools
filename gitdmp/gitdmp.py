#!/usr/bin/env python3

import zlib
import sys
import os

help_str="""
gitdmp 1.0.0

madeby: souvik (@DarthCucumber)

usage: gitdmp [-h] [-v] [-c] 

option:
    -c : dumps all the commit messages
    -v : dumps all the file changes of files in the git repo.
    -h : shows help menu
"""

#TODO: add ability to pass directory to the command

args=sys.argv[1:]

if len(args)==0:
    print("no options provided.")
    print(help_str)
    sys.exit(0)

target_dir=".git"
relative_path="./" 
target_files = os.path.join(relative_path,target_dir)

#if the dir is a git repo
if not os.path.exists(target_files) :
    print("Make sure this directory provided is a git repository")
    sys.exit(0)

#if the dir is empty:
dir_list=os.listdir(os.path.join(target_files,"objects")) 
if len(dir_list) == 0 or "pack" in dir_list or "info" in dir_list:
    print("empty .git/objects/\nno dump generated.")
    sys.exit(0)

#help flag
if "-h" in args:
   print(help_str)
   sys.exit(0)

#file content dump
if "-v" in args:
    print("\n=========[DUMP START]========\n")
    for subdir,dirs,files in os.walk(os.path.join(target_dir,"objects")):
        for file in files:
            fPath=os.path.join(subdir,file)
            buff_str=open(fPath,"rb").read()
            #decompressing the objects (file type zlib)
            fl_data=zlib.decompress(buff_str)
            print("\n===========["+fPath+"]===========\n")
            print(bytes(fl_data).decode('latin-1'))
    
    print("\n=========[DUMP END]========\n")

#commits dump
if "-c" in args:
    print("under construction")
    sys.exit(0)

