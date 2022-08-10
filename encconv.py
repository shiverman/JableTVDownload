
#-*- coding:utf-8 -*-
from distutils import filelist
import os
import subprocess

#遍历指定目录，显示目录下的所有文件名
def fileInFolder(filepath):
    pathDir = os.listdir(filepath) # 
    files = []
    for allDir in pathDir:
        child = os.path.join('%s\\%s' % (filepath, allDir))
        files.append(child) #

    return files


#遍历文件夹及其子文件夹的所有文件，获取文件的列表
def getfilelist(filepath):
    filelist = os.listdir(filepath)
    files = []
    for i in range(len(filelist)):
        child = os.path.join('%s\\%s' % (filepath, filelist[i]))
        if os.path.isdir(child):
            files.extend(getfilelist(child))
        else:
            files.append(child)
    return files
    
def mp42mkv(folder_path,file_name):
    try:
        subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4', '-c', 'copy',
                         f'{file_name}.mkv'])
        os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
        print(f"Encoded {file_name}")
    except:
        print(f"Fail to encode {file_name}")


xxx = "f:\\videos"

print(fileInFolder(xxx))
#print(getfilelist(xxx))

filelist = os.listdir(xxx)
for i in range(len(filelist)):
    filename = filelist[i]
    pathname = os.path.join(xxx,filename)
    if os.path.isdir(pathname):
        os.chdir(pathname)
        #pathname = os.getcwd()
        #filename = pathname.split(os.path.sep)[-1]
        print('现在转换第'+str(i+1)+'个文件')
        print(filename)
        mp42mkv(pathname,filename)
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)








