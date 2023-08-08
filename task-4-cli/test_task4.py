import pytest

from unittest.mock import patch

from task4 import open_read_file, count_single_characters, cli_parser


class TestOpenReadFile:

    def test_availability_file(self):
        with patch("builtins.open", side_effect=FileNotFoundError('Error: File missing or not found')):
            with pytest.raises(ValueError, match=r'Error: File missing or not found!'):
                open_read_file("file.txt")

    def test_read_file(self):
        with patch("builtins.open", side_effect=OSError("Can't read the file")):
            with pytest.raises(ValueError, match="Can't read the file"):
                open_read_file("file.txt")


class TestCliParser:

    def test_cli_parser(self):
        with patch('sys.argv', ['task4.py', '--string', 'Hello World']):
            args = cli_parser()
            assert args.string == 'Hello World'
            assert args.file is None

    with patch('sys.argv', ['task4.py', '--file', 'file.txt']):
        args = cli_parser()
        assert args.file == 'file.txt'
        assert args.string is None

    with patch('sys.argv', ['task4.py', '--string', 'Hello', '--file', 'file.txt']):
        # Перевірка, коли вказано обидва аргументи
        with pytest.raises(SystemExit):
            cli_parser()


class TestCountingFunction:

    def test_data_type(self):
        with pytest.raises(ValueError):
            count_single_characters(2632)

    @pytest.mark.parametrize('incoming_string, result_counting', [
        ('aabcccdss', 2),
        ('fgfggfhjk', 3),
        ('gggbvcd', 4),
        ('fgfggfhjk', 3),
        ('abcde', 5),
    ])
    def test_counting(self, incoming_string, result_counting):
        assert count_single_characters(incoming_string) == result_counting
