#!/usr/bin/env bash

# found a nice cheat sheet for bash which I used as a reference and its tutorial links:
        # https://devhints.io/bash
        # https://learnxinyminutes.com/docs/bash/
        # http://mywiki.wooledge.org/BashGuide

# download the README file
FILE=./README                                               # create variable for file
if [[ ! -e "$FILE" ]]; then                                 # check if the readme file doesn't exist
    wget 'ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README' # then download the README file
fi    

# make all text lowercase
TMP="$(tr [:upper:] [:lower:] < ${FILE})"

# split it into individual words per line (replace all spaces with newline, remove empty lines, remove punctuation)
TMP="$(echo "${TMP}" | sed 's/[[:space:]]/\n/g' | sed '/^$/d' | sed '/[[:punct:]]/d')"                       

# alphabetically sort the list of words and remove duplicates (with the number of occurences -c)
TMP="$(echo "${TMP}" | sort | uniq -c)"

# print out the 10 most common words in the text (without number of occurrences) on stdout
echo "${TMP}" | sort -rn | awk '{print $2}'| head
# echo "${TMP}" | sort -rn | cut -d' ' -f8 | head          # another method to do that
