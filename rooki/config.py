import os
import configparser

ROOKI_HOME = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CFG = os.path.join(ROOKI_HOME, 'default.cfg')

config = configparser.ConfigParser()
config.read(DEFAULT_CFG)
