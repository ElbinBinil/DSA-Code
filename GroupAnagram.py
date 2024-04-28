from collections import defaultdict

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = [""]


def checker(strs):
    anagram = defaultdict(list)
    result = []
    for s in strs:
        sorted_s = tuple(sorted(s))
        anagram[sorted_s].append(s)
    for values in anagram.values():
        result.append(values)
    return result


res = checker(strs)
print(res)


