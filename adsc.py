"""
Argumentative Dialogue Summary Corpus: Version 1.0
https://nlds.soe.ucsc.edu/node/30
"""

import os
import re
import json

DEFAULT_ADSC_FILENAME = "AllDialogs_phase1_Formatted.json"


def split_dialogue(text):
    pattern = re.compile(r'''(S\d:\d)''')
    return re.split(pattern, text)


def load_corpus(directory, filename=None):
    if filename is None:
        path = os.path.join(directory, DEFAULT_ADSC_FILENAME)
    else:
        path = os.path.join(directory, filename)

    with open(path) as fd:
        corpus = json.load(fd)

    return corpus
