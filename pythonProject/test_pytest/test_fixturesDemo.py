import pytest


@pytest.mark.usefixtures("setup")
class TestDemo:

    def test_method_6(self):
        print("It will execute method_1")

    def test_method_7(self):
        print("It will execute method_2")

    def test_method_8(self):
        print("It will execute method_3")
