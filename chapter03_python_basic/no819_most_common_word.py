import re
from collections import Counter, defaultdict
from typing import List

def most_common_word_my(paragraph: str, banned: List) -> str:
    string_sub = re.sub('[^a-zA-Z0-9]', ' ', paragraph)
    strings = [word.lower() for word in string_sub.split()]
    frequency = Counter(strings)
    if banned:
        for ban in banned:
            del frequency[ban]

    return frequency.most_common(1)[0][0]

def most_common_word(paragraph: str, banned: List) -> str:
    strings = [word for word in
               re.sub('[^\w]', ' ', paragraph).lower().split()
               if word not in banned]
    frequency = defaultdict(int)
    for word in strings:
        frequency[word] += 1
    return max(frequency, key=frequency.get)

print(most_common_word("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))