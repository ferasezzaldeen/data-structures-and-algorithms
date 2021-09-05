from repeted import *


def test_repeted_function():
    assert repeated_word('this is my first test in this cc')=='this'


def test_repeat_with_punctuation_marks():
    assert repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...')=='summer'


def test_repeted_function_with_capitals():
    assert repeated_word('This is my first test in this cc')=='this'
def test_repeted_function_with_faluier():
    assert repeated_word('This is my first')=='there is no repetetion'
