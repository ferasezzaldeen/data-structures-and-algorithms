from stack_queue_brackets import *

def test_test():

    assert 1+1


def test_hapyy():
    assert validate_brackets('{([])}')==True

def test_failuer():
    assert validate_brackets('{{{')==False

def test_edge_case():
    assert validate_brackets('{gbgbgbg}')==True
