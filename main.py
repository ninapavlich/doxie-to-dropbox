import time
import logging

from doxietodropbox.doxie import DoxieToDropbox

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s')



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