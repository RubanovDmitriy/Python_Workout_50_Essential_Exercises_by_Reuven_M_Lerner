from collections import Counter

import pytest

from exercise_21_tlw.exercise_21_log import status_codes_counter
from exercise_21_tlw.exercise_21_tlw import find_all_longest_words, find_longest_word


@pytest.fixture()
def empty_file(tmp_path):
    f = tmp_path / 'emptyfile.txt'
    f.write_text('')
    return f


@pytest.fixture()
def small_file(tmp_path):
    f = tmp_path / 'smallfile.txt'
    f.write_text('''This is the first line
and this is the second line''')
    return f


@pytest.fixture()
def big_file(tmp_path):
    f = tmp_path / 'bigfile.txt'
    f.write_text('''This is the first line of a big file
and this is the second line
and this is, to no one's surprise, the third line
but the biggest word will probably be encyclopedia''')
    return f


@pytest.fixture()
def log_file(tmp_path):
    f = tmp_path / 'logfile.txt'
    f.write_text('''67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"
66.249.71.65 - - [30/Jan/2010:00:12:06 +0200] "GET /browse/one_node/1557 HTTP/1.1" 200 39208 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
65.55.106.183 - - [30/Jan/2010:01:29:23 +0200] "GET /robots.txt HTTP/1.1" 200 99 "-" "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
65.55.106.183 - - [30/Jan/2010:01:30:06 +0200] "GET /browse/one_model/2162 HTTP/1.1" 200 2181 "-" "msnbot/2.0b (+http://search.msn.com/msnbot.htm)"
66.249.71.65 - - [30/Jan/2010:02:07:14 +0200] "GET /browse/browse_applet_tab/2593 HTTP/1.1" 200 10305 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.71.65 - - [30/Jan/2010:02:10:39 +0200] "GET /browse/browse_files_tab/2499?tab=true HTTP/1.1" 404 446 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:03:13:34 +0200] "GET /robots.txt HTTP/1.1" 404 99 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:03:13:34 +0200] "GET /browse/one_node/2715 HTTP/1.1" 404 26433 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:03:43:39 +0200] "GET /browse/download_model/1969 HTTP/1.1" 404 31713 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
66.249.65.12 - - [30/Jan/2010:04:05:43 +0200] "GET /browse/one_node/1406 HTTP/1.1" 302 118 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
''')
    return f


def test_small_file(small_file):
    assert find_longest_word(small_file) == 'second'


def test_big_file(big_file):
    assert find_longest_word(big_file) == 'encyclopedia'


def test_empty_directory(tmp_path):
    assert find_all_longest_words(tmp_path) == {}


def test_one_file(tmp_path, empty_file):
    assert find_all_longest_words(tmp_path) == {'emptyfile.txt': ''}


def test_all_files(tmp_path, empty_file, small_file, big_file):
    assert find_all_longest_words(tmp_path) == {'emptyfile.txt': '',
                                                'smallfile.txt': 'second',
                                                'bigfile.txt': 'encyclopedia'}


def test_status_codes_counter(log_file):
    assert status_codes_counter(log_file) == Counter({'200': 5, '404': 4, '302': 1})
