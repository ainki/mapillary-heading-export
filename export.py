import json
import os

from types import SimpleNamespace

foldernames= os.listdir (".mapillary/logs/")

y = {}
hs = open("headings.txt","x")

for foldername in foldernames: # loop through all the files and folders
    with open(".mapillary/logs/"+ foldername + "/sequence_process.json") as f:
            data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
            heading = data.MAPCompassHeading.TrueHeading
            save = {
                "file": foldername,
                "heading": heading
            }
    
            y = json.dumps(save)
            print(y)

            hs.write(y + "\n")
            
hs.close() 
