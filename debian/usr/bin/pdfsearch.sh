#!/bin/bash

SAVEIFS=$IFS
IFS=$'\n'

REG=$1
HOME=$2
for file in $(find $HOME -type f -name '*.odt'); do echo "$file" >> filelist.txt;done
if [ -f filelist.txt ]; then
    while read line; do unzip -c "$line" | grep --binary-files=text -oP "$REG" >> odt_grep.txt && echo "$line:$(cat odt_grep.txt)" && rm odt_grep.txt; done < filelist.txt
fi
rm -f filelist.txt rm odt_grep.txt
IFS=$SAVEIFS