# Script to simplify the file structure of a folder of folders
# Instead of a folder of folders with files, you get a folder with files

import os
import shutil

names = os.listdir('./images/')
# names.remove('.DS_Store')

i = 1
for f in names:
    p = './images/' + name
    if os.path.isdir(p):
        files = os.listdir(p)
        for f in files:
            os.rename(p + '/' + f, './images/' + str(i) + '.jpg')
            i += 1
        shutil.rmtree(p)
