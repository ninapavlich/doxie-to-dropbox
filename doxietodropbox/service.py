import time
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from doxie import DoxieToDropbox

LOG_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "doxietodropbox.log")
handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=2000, backupCount=10)
format = '%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s'
formatter = logging.Formatter(format)
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO,format=format)
logging.getLogger().addHandler(handler)


if __name__ == "__main__":
    import time

    doxie = DoxieToDropbox()
    
    try:
        if doxie.is_running:
            sys.exit("This app is already running!")
        
        while True:
            doxie.loop()
            time.sleep(30)

    finally:
        doxie.clean_up()