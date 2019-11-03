#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/19"


import mqtt_client as mqttc
import tnh as sensor

import time
import sys

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

import traceback

errCnt = 0

conf_mqtt = '/appli/conf/config_mqtt.yml'

def main():

    while 1:
        try:
            log.info('reading sensors values')
            payload = sensor.read()  

            log.info('sending payload to remote mqtt broker')
            mqttc.send_to_mqtt_broker(conf_mqtt, str(payload))
            log.info('sleeping for 30 min')
        except:
            errCnt += 1
            tb = traceback.format_exc()
            log.debug("!mqtt_client:\terrCnt: %s; last tb: %s" % (errCnt, tb))
        finally:
            time.sleep(1800)

# script entry point
if __name__ == '__main__':
    main()
