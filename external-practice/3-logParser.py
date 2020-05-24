#!/usr/bin/env python3

# https://pythonicways.wordpress.com/2016/12/20/log-file-parsing-in-python/

# Exports parsed data to a file

import re
import time
from time import strftime

log_file_path = r"C:\demo\sfbios.log"
export_file_path = r"C:\demo\filtered"

time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

file = "\\" + "Parser Output " + time_now + ".txt"
export_file = export_file_path + file

regex = '(<property name="(.*?)">(.*?)<\/property>)'
read_line = False

with open(log_file_path, "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
                print(match_text)
    else:
        data = file.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group()
            match_list.append(match_text)
file.close()

with open(export_file, "w+") as file:
    file.write("EXPORTED DATA:\n")
    match_list_clean = list(set(match_list))
    for item in range(0, len(match_list_clean)):
        print(match_list_clean[item])
        file.write(match_list_clean[item] + "\n")
file.close()