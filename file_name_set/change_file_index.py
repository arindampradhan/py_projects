$ ls
cheese_cheese_type.bar  cheese_cheese_type.foo
$ python
>>> import os
>>> for filename in os.listdir("."):
...  if filename.startswith("cheese_"):
...    os.rename(filename, filename[7:])
... 
>>> 
$ ls
cheese_type.bar  cheese_type.foo

# script for the workflow
# file names are sorted lexiographically
# change the names by index
# to index a huge list of files in a folder

!/usr/bin/env python
from os import rename, listdir


file_location = "C:\\paste_the_location_here"
i=0
for file_name in os.listdir(file_location):
	rename(file_name,str(i))
	i+=1	
