import os
from pathlib import Path
import subprocess
import sys


''' BASE_DIR is get the local file path'''
BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

''' file_path is jois the working env path '''
basic_packages_path = os.path.join(BASE_DIR/'python-package-installer/installed_packages.txt')
# print(file_path)

''' Write the packaes name in `need_packages.txt` you want to download '''
input = str(input("Enter the Package name ? "))
file_path_need = os.path.join(BASE_DIR/'python-package-installer/need_packages.txt')
with open(file_path_need,"w") as file_writing:
    # print(f"open => [{file_path_need}] ")
    input_conert = input.lower()
    file_writing.write(f"{input_conert}\n")