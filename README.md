#  dmenu-spell-checker

Word list provided by WordNet
https://wordnet.princeton.edu/download/current-version

Performed simple python processing to generate
some json documents of the WordNet content.

I then used these json documents to create a friendly
list of words and definitions which drives a dmenu
spell checker.

```
./mk_dmenu_words.py > words.txt
./spell.sh
```

By placing `spell.sh` in `/usr/local/bin` you can
easily call this utility from dmenu it self.

![Alt text](example.gif)

