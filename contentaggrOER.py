import pikepdf
import sys
import os
import urllib.request
from pathlib import Path
#import numpy as np
import pandas as pd
#get the target pdf file from the command-line arguments
pdf_url = sys.argv[1] #example https://bildungsportal.sachsen.de/opal/oer/10SYjW2AWSFYY

#creates temp dir if it doesn't exist
Path("temp").mkdir(parents=True, exist_ok=True)
#downloads the file to temp dir and names it temp
pdf_filename, headers = urllib.request.urlretrieve(pdf_url, "temp/temp")

# read the pdf file
pdf = pikepdf.Pdf.open(pdf_filename)
docinfo = pdf.docinfo

#create a dictionary and write document_info metadata in it
metadict = {}
for key, value in docinfo.items():  
    metadict.update({key:str(value)})
    
    #old Print Metadata to console
#    if "Array" in repr(value):
#        print(repr(key), ":", repr(value)) #todo this + Times
#    else:
#       print(key, ":", value)

#create a pandas Series element to save it
s = pd.Series(metadict)
s.to_csv("temp/meta.csv")
print("Saved to temp/meta.csv")
pdf.close() 
os.remove(pdf_filename)