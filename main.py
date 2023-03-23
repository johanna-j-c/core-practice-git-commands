import pytest


def always_returns_true():
    # Function is now returning True and this should always be true
    return True


def test_always_returns_true():
    assert always_returns_true()
