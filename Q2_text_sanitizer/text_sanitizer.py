import sys
import os
from collections import Counter

source = sys.argv[1] # ${1} : source (txt, cfg, database)
try : 
    target = sys.argv[2] # ${2} : target (cli, txt, database)
except :
    target = None

def connect_db(url) :
    if "://" in url :
        return(1)
    else :
        return(0)

if (os.path.exists(source)) & ("txt" in source):
    with open(source, "r", encoding="utf8") as f:
        txt_lines = f.readlines()
elif (os.path.exists(source)) & ("cfg" in source):
    with open(source, "r", encoding="utf8") as f:
        cfg_lines = [i.replace("\n","") for i in f.readlines()]
        source = cfg_lines[0]
        if target == None :
            try :
                target = cfg_lines[1]
            except :
                pass
        with open(source, "r", encoding="utf8") as f:
            txt_lines = f.readlines()
elif connect_db(source):
    print("Connect Database success")
else :
    raise Exception(f"{source} must be txt,cfg file or Database, please recheck again!!")

def statistic_calculation(txt_lines) :
    text = "".join(txt_lines)
    text_clean = text.lower()
    text_clean = text_clean.replace("\t", "____")
    text_count = dict(Counter(text_clean))
    text_count_clean =  {i:j for i,j in text_count.items() if i.isalpha()}
    text_count_sort = dict(sorted(text_count_clean.items(), key=lambda x: x[1], reverse=True))
    return [text, text_clean, text_count_sort]

list_data = statistic_calculation(txt_lines)
if (target == 'cli') | (target == None) :
    file_output = None
elif "txt" in target :
    f = open(target, 'w')
    file_output = f
elif connect_db(target):
    print("Connect Database success")

print("Raw Text : ", list_data[0], end = '\n', file=file_output)
print("Sanitized text : ", list_data[1], end = '\n', file=file_output)
print("Statistic calculation", file=file_output)
for i in list_data[2] :
    print(i," : ",list_data[2][i], file=file_output)

try : 
    f.close()
except :
    pass