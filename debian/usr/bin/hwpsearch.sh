#!/bin/bash

REG=$1
HOME=$2
find $HOME -type f -name '*.hwp' >> filelist.txt

if [ -f filelist.txt ]; then
    while read line; do /usr/local/bin/hwp5txt --output hwp_to_txt.txt "$line" && grep -oP "$REG" hwp_to_txt.txt >> hwp_grep.txt && echo "$line:$(cat hwp_grep.txt)" && rm hwp_grep.txt; done < filelist.txt
fi
rm -f filelist.txt hwp_to_txt.txt hwp_grep.txt
