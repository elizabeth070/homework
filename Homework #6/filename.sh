#!/bin/bash

echo -n "Enter a file or directory name: "
read filename

if [ ! -e "$filename" ]; then
    echo "Error: $filename does not exist"
    exit 1
fi

if [ -f "$filename" ]; then
    echo "$filename is a regular file"
elif [ -d "$filename" ]; then
    echo "$filename is a directory"
else
    echo "$filename is another type of file"
fi

ls -l "$filename"
