# Script to rename all .jpg files to .JPEG

import os
import shutil

names = os.listdir('./images/legos')

i = 1
for f in names:
    p = './images/legos/' + f
    if '.jpg' in f:
        os.rename(p, './images/legos/' + f.replace('.jpg', '.JPEG'))
        i += 1
