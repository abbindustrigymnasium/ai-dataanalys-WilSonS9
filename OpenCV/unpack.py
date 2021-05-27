# Script to simplify the file structure of a folder of folders
# Instead of a folder of folders of folders with files, you move all the files up a step, giving you a folder of folders with files

import os
import shutil

names = os.listdir('./legos/')
# names.remove('.DS_Store')

for name in names:
    p = './legos/' + name
    subs = os.listdir(p)
    i = 1
    for sub in subs:
        if os.path.isdir(p + '/' + sub):
            files = os.listdir(p + '/' + sub)
            for f in files:
                shutil.move(p + '/' + sub + '/' + f,  p)
                os.rename(p + '/' + f, p + '/' + str(i) + '.JPEG')
                i += 1
            shutil.rmtree(p + '/' + sub)
