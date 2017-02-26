from zipfile import ZipFile
import os
import re

def crack_prank(file):
    # extract file
    z = ZipFile(file, mode='r')
    print('Extracting {}...\n\n'.format(file))
    z.extractall()
    names = z.namelist()[5:]
    z.close()
    # loop through files and filter numbers
    for name in names:
        new_name = re.findall(r'\D+', name)
        new_name = ''.join(new_name)
        print(name, '\t - \t', new_name)
        os.rename(name, new_name)
        
crack_prank('prank.zip')
