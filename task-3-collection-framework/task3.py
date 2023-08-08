from collections import Counter

from functools import lru_cache


@lru_cache(maxsize=None)
def count_single_characters(incoming_string):

    if not isinstance(incoming_string, str):
        raise ValueError('The function works only with string data type!')

    characters = Counter(incoming_string)

    return sum(value for value in characters.values() if value == 1)

    # return sum(value for value in Counter(incoming_string).values() if value == 1)


if __name__ == '__main__':

    cases = ['aabcccdss', 'fgfggfhjk', 'gggbvcd', 'tfffffghhh', 'fgfggfhjk', 'abcde', 'abcde']

    for string in cases:
        print(f'incoming string : {string} , count single characters {count_single_characters(string)}')
