import argparse

from collections import Counter

from functools import lru_cache


# Функція відкриття файлу та читання даних. Повертає string
def open_read_file(file_name):

    try:
        with open(file_name, "r") as file:
            file_content = file.read()

    except FileNotFoundError:
        raise ValueError('Error: File missing or not found!')

    except OSError:
        raise ValueError("Can't read the file")

    except Exception as error:
        raise ValueError(f"Unexpected error: {error}")

    return file_content


# Ф-я створення CLI з аргументами --string та --file
def cli_parser():

    parser = argparse.ArgumentParser(description='CLI for string data processing')

    group = parser.add_mutually_exclusive_group()

    group.add_argument('--string', help='Input string for processing. !Use space between words!')
    group.add_argument('--file',
                       help='Enter the path and name of the text file. Content in file must have space between words')

    return parser.parse_args()


# Кешована ф-я з підрахунку к-сть повторюваних символів
@lru_cache(maxsize=None)
def count_single_characters(incoming_string):

    if not isinstance(incoming_string, str):
        raise ValueError('The function works only with string data type!')

    characters = Counter(incoming_string)

    return sum(value for value in characters.values() if value == 1)


if __name__ == '__main__':

    args = cli_parser()

    if args.file:

        string = open_read_file(args.file)

        for word in string.split():
            print(f'incoming string : {word} , count single characters {count_single_characters(word)}')

    if args.string:

        for word in args.string.split():
            print(f'incoming string : {word} , count single characters {count_single_characters(word)}')

    if not args.string and not args.file:

        cases = ['aabcccdss', 'fgfggfhjk', 'gggbvcd', 'tfffffghhh', 'fgfggfhjk', 'abcde', 'abcde']

        for word in cases:
            print(f'incoming string : {word} , count single characters {count_single_characters(word)}')
