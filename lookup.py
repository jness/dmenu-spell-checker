#!/usr/bin/env python3

import sys
import json


with open('words.json') as f:
    words = json.loads(f.read())

with open('word_definitions.json') as f:
    word_definitions = json.loads(f.read())

try:
    word = sys.argv[1]
except IndexError:
    print('Provide a word as input')
    sys.exit(1)

print(word)
print('-' * len(word))
for word_type, data_ids in words[word].items():
    print(f'{word_type}:')

    for data_id in data_ids:
        definition = word_definitions[data_id][word_type]
        print(f'  * {definition}')
