#!/usr/bin/env bash

# Found a nice cheat sheet for bash which I used as a reference and its tutorial links:
        # https://devhints.io/bash
        # https://learnxinyminutes.com/docs/bash/
        # http://mywiki.wooledge.org/BashGuide


                                        # download the README file
FILE=./README                               # create variable for file
if [[ -f "$FILE" ]]; then                   # check if the readme file already exists
    echo "$FILE already exists"             # print that the file already exists
else
    # TODO Check if this link already exists?
    wget 'ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README' # download the README file
fi    


tr [:upper:] [:lower:] < $FILE > TMP_FILE && mv TMP_FILE $FILE  # make all text lowercase


                                        # split it into individual words per line
sed -i 's/[[:space:]]/\n/g' $FILE           # replace all whitespaces with newline
sed -i '/^$/d' $FILE                        # remove empty lines 
sed -i 's/[[:punct:]]//g' $FILE             # remove punctuation


# alphabetically sort the list of words and remove duplicates (with the number of occurences -c)
cat < $FILE | sort | uniq -c > TMP_FILE && mv TMP_FILE $FILE


# print out the 10 most common words in the text (without number of occurrences) on stdout (uniq, sort, and head)
cat < $FILE | sort -r | awk '{print $2}'| head # man awk | grep 'print'

# TODO file without number of occurences?
