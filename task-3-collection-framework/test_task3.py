import pytest

from collections import Counter

from task3 import count_single_characters


class TestCountingFunction:

    def test_data_type(self):
        with pytest.raises(ValueError):
            count_single_characters(2632)

    @pytest.mark.parametrize("incoming_string", [
        "aabcccdss",
        "fgfggfhjk",
        "gggbvcd",
        "fgfggfhjk",
        "abcde"
    ])
    def test_characters_type(self, incoming_string):
        characters = Counter(incoming_string)
        assert isinstance(characters, dict)
        assert bool(characters)

    @pytest.mark.parametrize('incoming_string, result_counting', [
        ('aabcccdss', 2),
        ('fgfggfhjk', 3),
        ('gggbvcd', 4),
        ('fgfggfhjk', 3),
        ('abcde', 5),
    ])
    def test_counting(self, incoming_string, result_counting):
        assert count_single_characters(incoming_string) == result_counting


class TestCache:

    def test_cache_size(self):

        count_single_characters.cache_clear()  # Чистимо кеш перед тестуванням

        # Виклик функції з різними вхідними значеннями
        count_single_characters('aabcccdss')
        count_single_characters('fgfggfhjk')
        count_single_characters('gggbvcd')
        count_single_characters('fgfggfhjk')

        assert count_single_characters.cache_info().hits == 1  # Перевірка кількості попадань в кеш
        assert count_single_characters.cache_info().misses == 3  # Перевірка кількості промахів
        assert count_single_characters.cache_info().currsize == 3  # Перевірка поточного розміру кешу

    def test_cache_access(self):

        count_single_characters.cache_clear()  # Чистимо кеш перед тестуванням

        # Виклик функцій з однаковими вхідними значеннями
        result1 = count_single_characters('aabcccdss')
        '''
        При повторному виклику ф-ї з однаковим аргументом  - ф-я не виконується.
        Як результат в result2 отримуємо посилання на об'єкт result1.        
        '''
        result2 = count_single_characters('aabcccdss')

        assert result1 is result2  # Перевірка, що результати з однаковими вхідними значеннями беруться з кешу
