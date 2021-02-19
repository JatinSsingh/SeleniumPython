import logging


def test_logg():
    logger = logging.getLogger(__name__)

    filelocation = logging.FileHandler("logfile.log")
    format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filelocation.setFormatter(format)

    logger.addHandler(filelocation)
    logger.setLevel(logging.DEBUG)
    logger.debug("A Debug is executed")
    logger.info("Information statement")
    logger.warning("A Warning is Coming")
    logger.error("A Error is Coming")
    logger.critical("A Critical Message is Coming")
