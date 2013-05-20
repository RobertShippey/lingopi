import glob
from status import page_shows_warning

files = glob.glob("examples/*.txt")

current_page = ""

for file in files:
    f = open(file, 'r')
    current_page = f.read()
    f.close()
    e = page_shows_warning()
    print file, " returns ", e

print "Done"
