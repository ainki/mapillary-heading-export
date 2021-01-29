# mapillary-heading-export

With this tool you can export the headings of photos calculated using Mapillary tools to a text file.

Instructions:
1. With Mapillary tools use the command:
```
mapillary_tools process --user_name "YOUR MAPILLARY USERNAME" --advanced --import_path "PATH TO YOUR IMAGES" --rerun --advanced --interpolate_directions --verbose --duplicate_distance 0.5
```
This will process the images but not upload them to Mapillary.
2. Copy the export.py to the folder where .mapillary folder is located, or copy the .mapillary folder to this folder
3. Opem terminal and type ```python export.py```
4. Done
