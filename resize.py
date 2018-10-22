from PIL import Image
import glob, os
import argparse

size = 500, 300


def resize(path):

    for infile in glob.glob(path + "*.jpg"):
        print(infile)
        file, ext = os.path.splitext(infile)
        
        im = Image.open(infile)
        im.thumbnail(size)
        im.save(file + '-resized-'+ ".JPEG", "JPEG")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Resive images from a folder')
    parser.add_argument('--path', metavar='path', required=True,
                        help='the path to workspace')
    args = parser.parse_args()
    resize(args.path)
    # print(args.path)