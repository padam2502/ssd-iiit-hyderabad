#!/bin/bash
echo $(grep -o -i "\w\+*ing\+ " $1) | awk '{print tolower($0)}' | (sed 's/\s\+/\n/g') > $2 
#echo "Inside $2 file"
#cat $2
