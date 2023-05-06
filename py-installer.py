import os
from pathlib import Path
import subprocess
import sys


''' BASE_DIR is get the local file path'''
BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

''' file_path is jois the working env path '''
basic_packages_path = os.path.join(BASE_DIR/'python-package-installer/basic_packages.txt')
# print(file_path)

''' Write the packaes name in `need_packages.txt` you want to download '''
input = str(input("Enter the Package name ? "))
file_path_need = os.path.join(BASE_DIR/'python-package-installer/need_packages.txt')
with open(file_path_need,"w") as file_writing:
    # print(f"open => [{file_path_need}] ")
    input_conert = input.lower()
    file_writing.write(f"{input_conert}\n")
    

''' Write the packaes name in `installed_packages.txt` '''
# with open(basic_packages_path,"w") as file_writing:
#     print(f"open => [{basic_packages_path}] ")
#     reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
#     installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
#     for package in installed_packages:
#         file_writing.write(f"{package}\n")

''' Read the packaes name in `installed_packages.txt` '''      
with open(basic_packages_path,'rb') as file_writing:
    read = file_writing.read()
    # print(f"{read}")
    installed_basic_packages_path = [r.decode().split('\r')[0] for r in read.split()]
    print(f"{installed_basic_packages_path}")
    for package in installed_basic_packages_path:
        print(package)
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])