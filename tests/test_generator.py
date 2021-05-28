import unittest
from generator import generator as main


def test_sample_single_word():
    array = ('foo', 'bar', 'foobar')
    word = main.sample(array)
    assert word in array


def test_sample_multiple_words():
    array = ('foo', 'bar', 'foobar')
    words = main.sample(array, 2)
    assert len(words) == 2
    assert words[0] in array
    assert words[1] in array
    assert words[0] is not words[1]


def test_recepie():
    its = ['item1', 'item2']
    acts = ['act1', 'act2']
    result_wait = 'Рецепт:\n' + '1) act1 item1\n'+'2) act2 item2\n' + 'Готово!'
    result_have = main.get_recepie(its, acts)
    assert result_wait == result_have
