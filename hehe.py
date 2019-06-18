import os
import re

fuck = 0

def get_file_path(root_path, file_list, dir_list):
    dir_or_files = os.listdir(root_path)
    global fuck
    for dir_file in dir_or_files:
        # 获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, dir_file)
        # 判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            # 递归获取所有文件和目录的路径
            get_file_path(dir_file_path, file_list, dir_list)
        else:
            file_list.append(dir_file_path)
            if re.search(r'.*.\.max',dir_file_path):
                print (dir_file_path)
                f.write(dir_file_path+"\n")
                fuck = fuck + 1
        

root_path = '/var/www/owncloud/data'
file_name = os.listdir('/var/www/owncloud/data')
file_list = []
dir_list = []
f = open("data.txt","w")
for dir_file in file_name:
    dir_file_path = os.path.join(root_path, dir_file)
    if os.path.isdir(dir_file_path):
        if re.search(r'[A-Z]',dir_file_path):
            userid = dir_file_path
            print(userid)
            f.write(userid+"\n")
            get_file_path(dir_file_path,file_list,dir_list)
            print(fuck)
            f.write(str(fuck))
            f.write("\n"+"\n")
            fuck = 0
f.close()
       
