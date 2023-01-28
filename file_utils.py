import os
import tarfile

def zip(path, file_name):
    file_obj= tarfile.open(file_name+".tar","w")
    file_obj.add(path)
    file_obj.close()
    
def extract(file_path, folder_path):
    file_obj= tarfile.open(file_path)
    file_obj.extractall(folder_path)
    file_obj.close()
    
def delete(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print('File not found to be deleted')

def list_all_files_in_folder(folder_path):
    entries = os.listdir(folder_path)
    print(entries)