import os
from pathlib import Path


''' BASE_DIR is get the local file path'''
BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)

''' file_path is jois the working env path '''
file_path = os.path.join(BASE_DIR/'python-package-installer/installed_packages.txt')
# print(file_path)

