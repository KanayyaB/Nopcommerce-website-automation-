import logging

class Loggen:
    @staticmethod
    def logs():
        logger = logging.getLogger()
        filehandler = logging.FileHandler(filename=".\\logs\\automation.log")
        format = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(format)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger








