import unittest

from anagrams import reverse_text, reverse_word

from parameterized import parameterized


class TestAnagrams(unittest.TestCase):

    @parameterized.expand([
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', ''),
        ('a2b!c1d# h$g8f@e3', 'd2c!b1a# e$f8g@h3')
    ])
    def test_reverse_words(self, incoming_string, reversed_string):
        self.assertEqual(reverse_text(incoming_string), reversed_string)

    @parameterized.expand([
        ('abcd', 'dcba'),
        ('efg!h', 'hgf!e'),
        ('', ''),
        ('h$g8f@e3', 'e$f8g@h3')
    ])
    def test_reverse_word(self, incoming_word, reversed_word):
        self.assertEqual(reverse_word(incoming_word), reversed_word)

    def test_data_type(self):
        self.assertRaises(ValueError, reverse_text, 2632)


if __name__ == '__main__':
    unittest.main()
