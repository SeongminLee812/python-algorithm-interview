from typing import List
from collections import defaultdict

def group(strs: List[str]) -> List[List[str]]:
    gram_dict = {}
    word_list = []
    for original in strs:
        sort_word = ''.join(sorted(original))
        gram_dict.setdefault(sort_word, []).append(original)
        word_list.append(sort_word)
    result_list = [value for value in gram_dict.values()]

    return result_list

def group(strs: List[str]) -> List[List[str]]:
    gram_dict = defaultdict(list)
    word_list = []
    for original in strs:
        sort_word = ''.join(sorted(original))
        gram_dict[sort_word].append(original)
        word_list.append(sort_word)
    result_list = [value for value in gram_dict.values()]

    return result_list

print(group(["",""]))
print(group(["eat","tea","tan","ate","nat","bat"]))
print(group([""]))
