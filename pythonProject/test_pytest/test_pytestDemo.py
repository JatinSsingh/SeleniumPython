import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_method():
    print("Hello! World")


@pytest.mark.xfail
def test_method2():
    a = 3
    assert a + 3 == 10


def test_method4(setup):
    print('It will execute after method3')


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
