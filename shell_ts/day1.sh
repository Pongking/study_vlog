#!/bin/bash

#use ` to assign the result of the formula to variable 
suffix=`date +%Y%m%d` 

for f in `find ./data/ -type f -name "*.txt_"`
do
    echo "backup the file $f"
    cp ${f} ${f}_${suffix}
done
