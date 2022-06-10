import pikepdf
import sys
#import os
import urllib.request
from pathlib import Path

#get the target pdf file from the command-line arguments
pdf_url = sys.argv[1] #example https://bildungsportal.sachsen.de/opal/oer/8I6sM5zapD60

#creates temp dir if it doesn't exist
Path("temp").mkdir(parents=True, exist_ok=True)
#downloads the file to temp dir and names it temp
pdf_filename, headers = urllib.request.urlretrieve(pdf_url, "temp/temp")
    # get the target pdf file from the command-line arguments
    #pdf_filename = sys.argv[1]
    #print(pdf_filename)
# read the pdf file
pdf = pikepdf.Pdf.open(pdf_filename)
docinfo = pdf.docinfo
for key, value in docinfo.items():
    if "Array" in repr(value):
        print(repr(key), ":", repr(value)) #todo this + Times
    else:
        print(repr(key), ":", value)

#os.remove(pdf_filename)