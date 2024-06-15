#!/usr/bin/env python3

import sys
import json
import re
from glob import glob

word_types = ['noun', 'verb', 'adj', 'adv']

content = {}
for word_type in word_types:
    with open(f'dict/index.{word_type}') as f:
        data = [ i.strip() for i in f.read().split('\n') if i ]
        for line in data:

            # match word line pattern
            search = re.search('\\S+ \\S ', line)

            if search:
                word = line.split()[0]
                data_ids = re.findall('[0-9]{8}', line)

                if word not in content:
                    content[word] = {}

                content[word][word_type] = data_ids

print(json.dumps(content, indent=2))

