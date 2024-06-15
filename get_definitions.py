#!/usr/bin/env python3

import sys
import json
import re
from glob import glob

word_types = ['noun', 'verb', 'adj', 'adv']

content = {}
for word_type in word_types:
    with open(f'dict/data.{word_type}') as f:
        data = [ i.strip() for i in f.read().split('\n') if i ]
        for line in data:

            # match definition line pattern
            search = re.search('^[0-9]{8} ', line)

            if search:
                data_id = line.split()[0]
                desc = line.split(' | ')[-1].strip()

                if data_id not in content:
                    content[data_id] = {}

                content[data_id][word_type] = desc

print(json.dumps(content, indent=2))

