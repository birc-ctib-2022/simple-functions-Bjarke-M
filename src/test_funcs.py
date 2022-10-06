# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from funcs import (
    prod,
    prod2,
    longest,
    dist
)


def test_prod():
    assert prod(1, 2, 3) == 6
    assert prod(1,1,1) == 1
    assert prod(1,1,0) == 0


def test_prod2():
    assert prod2(42) == 378
    assert prod2(42) == prod(3,3,42)


def test_longest():
    assert longest([1, 2, 3], [4, 5]) == [1,2,3]
    assert longest([],[]) == []


def test_dist():
    assert dist((1, 2), (3, 4)) == 2.8284271247461903
