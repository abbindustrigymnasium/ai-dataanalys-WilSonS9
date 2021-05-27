# Script to add the .JPEG extension to all files

import os
import shutil

names = os.listdir('./legos/')
# names.remove('.DS_Store')

for name in names:
    p = './legos/' + name
    files = os.listdir(p)
    i = 1
    for f in files:
        os.rename(p + '/' + f, p + '/' + str(i) + '.JPEG')
        i += 1
