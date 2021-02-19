import pytest

from test_pytest.BaseClass import TestLog


class TestLogg(TestLog):

    @pytest.mark.usefixtures("data")
    def test_fixtureData(self, data):
        log = self.test_logg()
        log.info(data)
        print(data)
