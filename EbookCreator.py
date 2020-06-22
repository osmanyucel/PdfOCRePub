from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pytesseract

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(initialdir="/media/osmanyucel/TOSHIBA EXT/personal/Calibre Library/") # show an "Open" dialog box and return the path to the selected file
print(filename)

from pdf2image import convert_from_path

outfile = filename[:-3]+"htm"
print(outfile)
i =1
while i<1000:
    images_from_path = convert_from_path(filename, first_page=i, last_page=i)
    if not images_from_path:
        break
    paragraph= ""
    for file in images_from_path:
        page = pytesseract.image_to_string(file, lang="tur")
        with open(outfile, "a") as fout:
            
            for line in page.splitlines():
                if line == "":
                    fout.write("<p>" + paragraph + "</p>\n")
                    print(paragraph)
                    paragraph = ""
                else:
                    if line.endswith("—") or line.endswith("-"):
                        paragraph = paragraph + "" + line[:-1]
                    else:
                        paragraph = paragraph + " "+ line
            fout.write("<p>" + paragraph + "</p>")
    i= i+1
fout.close()
print(outfile)
