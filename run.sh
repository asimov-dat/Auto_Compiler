#!/bin/bash

if [$# -eq 0]
then 
    python3 get_files.py 
fi

if ! [$# -eq 0]
then
    python3 get_files.py $1 $2
fi

file_paths=()
index=0
while read line;
do
    file_paths+=($line)
    #index+=1
done < "files.txt"
# declare -p file_paths

# echo ${#file_paths[@]}

# echo "${file_paths[@]}"

case $1 in
    
    c)
        CMD="gcc "
        for file in "${file_paths[@]}"
        do
            CMD+="$file  "
        done

        eval $CMD

        ./a.out
        ;;

    test) # this does not work in c
        for file in "${file_paths[@]}"
        do 
            gcc "$file"
        done
        ls -l a.out
        ./a.out
        ;;
    *)
        echo "Invalid language"
        ;;
    
esac
