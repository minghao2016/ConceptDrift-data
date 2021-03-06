#!/usr/bin/env python

# LOVHarvester.py: A Linked Data vocabulary version harvester using
# the lov.okfn.org REST API

import logging
from ConfigParser import SafeConfigParser
from common.LOVVersions import LOVVersions
from common.LOVDSGenerator import LOVDSGenerator

CONFIG_INI = "config.ini"

class LOVHarvester:

    def __init__(self, __config):
        '''
        Class constructor
        '''
        self.log = logging.getLogger('LOVHarvester')

        self.config = __config
        self.LOV_DETAIL = self.config.get('lov', 'detail')

        self.log.info("Retrieving LOV version metadata...")
        ver = LOVVersions(self.config)
        self.log.debug(ver.getVersions())
        self.log.info("Serializing LOV version metadata...")
        ver.serializeVersions()

        self.log.info("Retrieving and serializing LOV version data...")
        gen = LOVDSGenerator(self.config)

        self.log.info("All done.")

if __name__ == "__main__":
    # Config
    config = SafeConfigParser()
    config.read(CONFIG_INI)
    
    # Logging
    logLevel = logging.INFO
    if config.get('general', 'verbose') == 1:
        logLevel = logging.DEBUG
    logging.basicConfig(level=logLevel)
    logging.info("Initializing...")

    # Instance
    l = LOVHarvester(config)
    logging.info("Exiting...")
    exit(0)
