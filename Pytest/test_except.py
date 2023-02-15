import pytest


def f():
    # raises helper raises an exception
    raise KeyboardInterrupt(0)


def test_mytest():
    with pytest.raises(KeyboardInterrupt):
        f()