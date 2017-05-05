import time
import os

relative_path = "OOP/"
target_chars = "0123456789"

def rename_files() :
    print "This Program started on" + time.ctime()
    # (1) get file names from a folder
    # saved_path = os.getcwd() 
    file_list = os.listdir(relative_path)
    for e in file_list :
        print e

    # (2) for each file, rename filename
    for file_name in file_list:
        # os.rename(file_name, file_name.translate(None, target_chars))
        # WindowsError: [Error 2] The system cannot find the file specified
        os.rename(os.path.join(relative_path, file_name),
                  os.path.join(relative_path, file_name.translate(None, target_chars)))


rename_files()
