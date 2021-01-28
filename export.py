import json
import os

directory = os.walk('/')
data = json.load(open('test.json'))
print(data)
print(directory)
