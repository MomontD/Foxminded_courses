def reverse_word(word, letters):

    result = []

    for char in word:
        if not char.isalpha():
            result.append(char)
        else:
            result.append(letters.pop())

    return ''.join(result)


def reverse_text(incoming_text):

    list_words = incoming_text.split()
    reverse_words = []

    for word in list_words:

        letters = [char for char in word if char.isalpha()]

        reverse_words.append(reverse_word(word, letters))

    return ' '.join(reverse_words)


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', '')
    ]

    for text, reversed_text in cases:
        assert reverse_text(text) == reversed_text

# Нижче не мій код, знайшов неті.
# Вирішив закомітити. Красиво написаний - необхідна ф-я в 3 рядка.

# s = 'a2b!c1d'
# letters = [char for char in s if char.isalpha()]
# reversed_letters = letters[::-1]
# result = ''.join(char if not char.isalpha() else reversed_letters.pop(0) for char in s)