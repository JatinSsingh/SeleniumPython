import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class Baseclass:

    def test_logg(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        filelocation = logging.FileHandler("logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filelocation.setFormatter(format)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filelocation)
        logger.setLevel(logging.DEBUG)
        return logger
