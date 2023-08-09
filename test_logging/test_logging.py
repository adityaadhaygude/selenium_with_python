from loggerClass import LoggerClass

# Note: if logs are not integrated in the html report then add flag --capture sys 
# example: py.test test_logging.py -s --html=report.html --capture sys


class TestLogger(LoggerClass):
    def test_loggingDemo(self):

        #create a logging object
        log = self.getLoggerNow()
        print("Hello")
        #following methods are used to print level wise logs
        log.info("This is our first log")
        log.warning("Something is missing")
        log.error("404 file not found")
        log.debug("file name is " + __name__)
        log.critical("This is critical section")