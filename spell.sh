#!/bin/bash

word_line=`cat words.txt | dmenu -i -l 25 -p "Word: " | tr -d '\n'`
word=$(echo "$word_line" | awk -F' :' '{print $1}')

echo -n "$word" | xclip -selection clipboard
