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

outfile = io.open("outfile.html", mode="w+", encoding="utf-8")

outfile.write('<meta charset="utf-8"><html><head>'\
              + '<title>Folder: ' \
              + sys.argv[1] + '</title>')

outfile.write('<link rel="stylesheet" type="text/css"'
              + ' href="style.css"></head><body>')

# start table and first row
outfile.write("<table><tbody><tr>")

images = os.listdir(sys.argv[1])

for i, image in enumerate(images, 1):
    outfile.write('<td><img src="'\
                  + sys.argv[1] + '/' + image\
                  + '" /></td>')
    outfile.write('<td><input type="text" /></td>')
    
    if i % TABLE_COLS == 0:
        outfile.write("</tr><tr>")

    
    
outfile.write('</tbody></table><br><br> <textarea rows="'\
              + str(TEXT_ROWS) + '" cols="' + str(TEXT_COLS)\
              + '"></textarea>')

outfile.write("</body></html>")
outfile.close()

print("Done")
