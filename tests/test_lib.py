# tests/test_lib.py
from psycovid.lib import hello_world

def test_length_of_hello_world():
    assert len(hello_world()) != 0
    