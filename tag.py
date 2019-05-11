import os
import io
import sys

TABLE_COLS = 4
TEXT_ROWS = 8
TEXT_COLS = 100

if not len(sys.argv) == 2:
    print("Usage: " + sys.argv[0] \
          + " <path to image folder>")
    quit()

out = '<meta charset="utf-8"><html><head>' \
    + '<title>Folder: ' \
    + sys.argv[1] + '</title>' \
    + '<link rel="stylesheet" type="text/css"' \
    + ' href="style.css"></head><body>' \
    + "<table><tbody><tr>"

images = os.listdir(sys.argv[1])

for i, image in enumerate(images, 1):
    out += '<td><img src="'\
        + sys.argv[1] + '/' + image\
        + '" />'\
        + '\n<input type="text" /></td>'
    
    if i % TABLE_COLS == 0:
        out += "</tr><tr>"

    
    
out += '</tbody></table><br><br> <textarea rows="'\
    + str(TEXT_ROWS) + '" cols="' + str(TEXT_COLS)\
    + '"></textarea>' \
    + "</body></html>"

outfile = io.open("outfile.html", mode="w+", encoding="utf-8")
outfile.write(out)
outfile.close()

print("Done")
