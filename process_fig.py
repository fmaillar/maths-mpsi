# -*- coding: utf-8 -*-

import os

scriptname = os.path.basename(__file__)

relevant_path = "./"
included_extensions = ['py']
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]
index = file_names.index(scriptname)
file_names.pop(index)
#print(file_names)

for file in file_names:
    os.system('python '+file)
