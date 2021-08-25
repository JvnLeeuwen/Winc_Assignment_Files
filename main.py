__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

from os import chdir
import os.path
import shutil
import zipfile

def clean_cache():
    if os.path.isdir("./cache"):
        #cache exits
        shutil.rmtree('./cache')
        os.mkdir("cache")
    else: 
        #cache doesn't exist
        os.mkdir("cache")
    return

def cache_zip(zip_file_path,cache_dir_path):
    data_zip = zipfile.ZipFile(zip_file_path, 'r')
    data_zip.extractall(path=cache_dir_path)
    return

def cached_files():
    basepath = os.path.join(os.getcwd(),"cache")
    print(basepath)
    file_list = []
    for entry in os.listdir(basepath):
        entry_path= os.path.join(basepath, entry)
        if os.path.isfile(entry_path):
           file_list.append(entry_path)
    return file_list

def find_password(file_list):
    for file_name in file_list:
        with open(file_name, 'r') as reader:
            for line in reader.readlines():
                if line.find("password")!=-1:
                    return line[10:-1]
    return "No password found"
                    
    


#print(os.getcwd())
#os.chdir("./files")
#print(os.getcwd())
#os.chdir("PythonAssignments/files")


#clean_cache()
#cache_zip("data.zip",".\cache")
#list = cached_files()
#print(find_password(list))





