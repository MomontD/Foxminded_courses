import pytest

from unittest.mock import patch

from src.report_monaco_2018.file_report import read_file, build_report, RacerData, print_report


class TestOpenReadFile:

    def test_availability_file(self):
        with patch("builtins.open", side_effect=FileNotFoundError('Error: File missing or not found')):
            with pytest.raises(ValueError, match=r'Error: File missing or not found!'):
                read_file("abbreviations.txt", 'logs')
                read_file("start.log", 'logs')
                read_file("end.log", 'logs')

    def test_read_file(self):
        with patch("builtins.open", side_effect=OSError("Can't read the file")):
            with pytest.raises(ValueError, match="Can't read the file"):
                read_file("abbreviations.txt", 'logs')
                read_file("start.log", 'logs')
                read_file("end.log", 'logs')


class TestBuildReport:

    def test_build_report(self):

        data = build_report('logs')

        assert isinstance(data, dict)

        for instance in data.values():

            assert isinstance(instance, RacerData)


class TestPrintReport:

    def test_print_report(self):

        data = build_report('logs')

        report = print_report(data)

        assert isinstance(report, list)

        for instance in report:

            assert isinstance(instance, RacerData)