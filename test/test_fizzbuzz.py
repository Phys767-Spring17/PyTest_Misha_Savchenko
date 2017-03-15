from fizzbuzz.FizzBuzz import fizzbuzz
import pytest

def test_fizzbuzz_1():

    assert fizzbuzz(1) == 1

def test_fizzbuzz_2():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz_3():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz_3():
    assert fizzbuzz(15) == "fizzbuzz"


def test_fizzbuzz_4():
    for x in range(100,4):
        if x % 3 == 0 and x % 5 != 0:
            assert fizzbuzz(x) == "fizz"
        elif x % 5 == 0 and x % 3 != 0:
            assert fizzbuzz(x) == "buzz"
        elif x % 3 == 0 and x % 5 == 0:
            assert fizzbuzz(x) == "fizzbuzz"
        else:
            assert fizzbuzz(x) == x
