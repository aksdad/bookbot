from collections import defaultdict
from typing import Dict, List

def get_num_words(contents: str) -> int:
    return len(contents.split())

def get_char_freq(contents: str) -> Dict[str, int]:
    d = defaultdict(int)
    for c in contents:
        ch = c
        if ch.isalpha():
            ch = ch.lower()
        d[ch] += 1
    return d

def sorted_char_freq(contents: str) -> List[Dict[str, int]]:
    char_freqs = get_char_freq(contents)
    freqs = list(char_freqs.items())
    freqs.sort(key= lambda x: x[1], reverse=True)
    out = []
    for k, v in freqs:
        out.append({"char": k, "num": v})
    return out


