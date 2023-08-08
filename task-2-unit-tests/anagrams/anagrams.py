def reverse_word(word):

    letters = [char for char in word if char.isalpha()]

    result = []

    for char in word:
        if not char.isalpha():
            result.append(char)
        else:
            result.append(letters.pop())

    return ''.join(result)


def reverse_text(incoming_text):

    if not isinstance(incoming_text, str):
        raise ValueError('The function works only with string data type!')

    list_words = incoming_text.split()
    reverse_words = []

    for word in list_words:

        reverse_words.append(reverse_word(word))

    return ' '.join(reverse_words)


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', ''),
        ('a2b!c1d# h$g8f@e3', 'd2c!b1a# e$f8g@h3')
    ]

    for text, reversed_text in cases:
        assert reverse_text(text) == reversed_text
