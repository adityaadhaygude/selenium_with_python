import logging

class LoggerClass:
    def getLoggerNow(self):

        logger = logging.getLogger(__name__)
        
        fileHandler = logging.FileHandler("test.log")
        logger.addHandler(fileHandler)

        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)

        return logger