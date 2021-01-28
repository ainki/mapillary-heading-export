import json
import os

foldernames= os.listdir (".mapillary/logs/")

result = []

for foldername in foldernames: # loop through all the files and folders
    with open(".mapillary/logs/"+ foldername + "/sequence_process.json") as f:
        data = json.load(f)
        heading = data["MAPCompassHeading"]
        save = {
            "file": foldername,
            "heading": heading
        }
        print(json.dumps(save))

print(result)