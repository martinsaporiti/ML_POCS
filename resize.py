from PIL import Image
import glob, os

size = 500, 300

for infile in glob.glob("*.JPG"):
    print(infile)
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save('thumbnail/' + file + ".thumbnail.JPEG", "JPEG")