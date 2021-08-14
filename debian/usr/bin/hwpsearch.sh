#!/bin/bash

SAVEIFS=$IFS
IFS=$'\n'

REG=$1
HOME=$2
for file in $(find $HOME -type f -name '*.hwp'); do echo "$file" >> filelist.txt;done
while read line; do /usr/local/bin/hwp5txt --output hwp_to_txt.txt "$line" && grep -oP "$REG" hwp_to_txt.txt >> hwp_grep.txt && echo "$line:$(cat hwp_grep.txt)" && rm hwp_grep.txt; done < filelist.txt
rm filelist.txt hwp_to_txt.txt hwp_grep.txt

IFS=$SAVEIFS