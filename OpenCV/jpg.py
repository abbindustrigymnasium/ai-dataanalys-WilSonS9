# Script to simplify the file structure of a folder of folders
# Instead of a folder of folders with files, you get a folder with files

import os
import shutil

names = os.listdir('./images/legos')
# names.remove('.DS_Store')

i = 1
for f in names:
    p = './images/legos/' + f
    if '.jpg' in f:
        os.rename(p, './images/legos/' + str(i) + '.jpg')
        i += 1