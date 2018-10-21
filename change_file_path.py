from os import listdir
from os.path import isfile, join
import argparse
from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

def change(scan, path):

    onlyfiles = [f for f in listdir(scan) if isfile(join(scan, f))]
    
    if not scan.endswith('/'):
        scan += '/'

    for file in onlyfiles:

        full_path = scan + file

        print('Process File: ', file)
        if file.endswith('.xml'):
            new_name = change_name(file)

            tree = ET.parse(full_path)
            root = tree.getroot()
            root[1].text = new_name + '.JPEG'
            root[2].text = path + new_name + '.JPEG'
            tree.write(full_path)

            # Cambio el nombre del xml si contiene el substring thumbnail
            if('thumbnail' in file):
                name_as_array = file.split('.')
                file = name_as_array[0] + '.xml'
                os.rename(full_path, scan + file)

        else: 
            if('thumbnail' in file):
                name_as_array = file.split('.')
                file = name_as_array[0] + '.JPEG'
                os.rename(full_path, scan + file)
            else:
                name_as_array = file.split('.')
                file = name_as_array[0] + '.JPEG'
                os.rename(full_path, scan + file)






def change_name(file_name):
    name_as_array = file_name.split('.')
    return name_as_array[0]
    




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Util')
    parser.add_argument('--scan', metavar='path', required=True,
                    help='The directory path')
    parser.add_argument('--path', metavar='path', required=True,
                    help='The new path ')
    args = parser.parse_args()
    change(args.scan, args.path)