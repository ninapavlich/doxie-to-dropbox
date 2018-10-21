import os
import sys
import copy
import re
import logging
from shutil import copyfile


"""
Managing Django Environment Variables
http://www.wellfireinteractive.com/blog/easier-12-factor-django/
"""

def get(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.environ.get(key, default)
    
    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val

def read(env_file=".env"):
    """
    Pulled from Honcho code with minor updates, reads local default
    environment variables from a .env file located in the project root
    directory.
    """
    try:
        with open(env_file) as f:
            content = f.read()

    except IOError:
        content = ''

    for line in content.splitlines():

        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            os.environ.setdefault(key, val)

# -- Read .env Variables
if 'DROPBOX_TO_DOXIE_CONFIG' in os.environ:
    config_file = os.environ["DROPBOX_TO_DOXIE_CONFIG"]
else:
    from os.path import expanduser
    home = expanduser("~")
    config_file = os.path.join(home, "dropboxtodoxie.conf")
    if not os.path.exists(config_file):
        logging.error("WARNING: Please edit the dropbox-to-doxie config file, located at %s, and then re-run this script. Script will not work correctly until this is done."%(config_file))
        config_template = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "example.env")
        copyfile(config_template, config_file)
        sys.exit()


read(env_file=config_file)
    
        



DOXIE_SERVER = get("DOXIE_SERVER")
DOXIE_USERNAME = get("DOXIE_USERNAME")
DOXIE_PASSWORD = get("DOXIE_PASSWORD")
DOXIE_FOLDER = get("DOXIE_FOLDER")
DROPBOX_ACCESS_TOKEN = get("DROPBOX_ACCESS_TOKEN")

if not DROPBOX_ACCESS_TOKEN:
    logging.error("WARNING: Dropbox access token was left empty in the config file, located at %s. Please add your dropbox access token and re-run this script."%(config_file))
    sys.exit()    
