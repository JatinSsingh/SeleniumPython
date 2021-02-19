import pytest


@pytest.fixture()
def setup():
    print('It will execute first')
    yield
    print('It will execute at last')


@pytest.fixture()
def data():
    print('User Profile Data is Created')
    return ['Jatin', 'Ssingh', 'Software Test Engineer']


@pytest.fixture(params=[("Chrome", "Jatin", "Ssingh"), ("Firefox", "Software Test Engineer"), "IE"])
def crossBrowser(request):
    return request.param
