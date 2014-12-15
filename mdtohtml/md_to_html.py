#pip install markdown2
#usage
#=====
#python md_to_html.py <filename>

import markdown2
import sys



f = open(sys.argv[1],'r')

fext = f.name.split('.')[1]
fname = f.name.split('.')[0]

if fext == "md":
    fhtml_str = markdown2.markdown(f.read())
    with open(fname+".html","w") as fl:
        fl.write("{}".format(fhtml_str))
else:
    print "The file is not a markdown extension"
