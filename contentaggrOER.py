import pikepdf
#import sys
#import os
import urllib.request

pdf_filename, headers = urllib.request.urlretrieve("https://bildungsportal.sachsen.de/opal/oer/1zfzKOhH3Szw")
    # get the target pdf file from the command-line arguments
    #pdf_filename = sys.argv[1]
print(pdf_filename)
# read the pdf file
pdf = pikepdf.Pdf.open(pdf_filename)
docinfo = pdf.docinfo
for key, value in docinfo.items():
    if "Array" in repr(value):
        print(repr(key), ":", repr(value)) #todo this + Times
    else:
        print(repr(key), ":", value)

#os.remove(pdf_filename)