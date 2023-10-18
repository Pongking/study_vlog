#!/bin/bash

#use ` to assign the result of the formula to variable 
#like to define a function

suffix=`date +%Y%m%d` 

for f in `find ./data/ -type f -name "*.txt"`
do
    echo "backup the file ${f}"
    # echo "backup the file $f"
    cp ${f} ${f}_${suffix}
done
