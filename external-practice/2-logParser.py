#!/usr/bin/env python3

# https://pythonicways.wordpress.com/2016/12/20/log-file-parsing-in-python/

# Parses more than one line

import re

log_file_path = r"C:\demo\sfbios.log"

regex = '(<property name="(.*?)">(.*?)<\/property>)'

read_line = True

with open(log_file_path, "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
                print(match_text)
    else:
        data = f.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group()
            match_list.append(match_text)
file.close()