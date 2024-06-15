#!/usr/bin/env python3

import re
import sys
import json


with open('words.json') as f:
    words = json.loads(f.read())

with open('word_definitions.json') as f:
    word_definitions = json.loads(f.read())

for word, data_ids in words.items():

    word_type = list(words[word].keys())[0]
    data_id = words[word][word_type][0]

    try:
        definition = word_definitions[data_id][word_type]
        if '-' not in word and '_' not in word and '.' not in word and "'" not in word:
            if not re.search('[0-9]', word):
                print(f'{word} : ({word_type}) - {definition}')
    except KeyError:
        pass

