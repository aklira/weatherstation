#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/19"

import paho.mqtt.client as paho
import yaml

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

import traceback

def read_mqtt_config(conf_file):
    with open(conf_file, 'r') as config:
        out = yaml.load(config)
    return out

def send_to_mqtt_broker(conf_file, payload):

    mqtt_conf = read_mqtt_config(conf_file)
    host = mqtt_conf['host']
    port = mqtt_conf['port']
    #user = mqtt_conf['user']
    #pwd = mqtt_conf['pwd']
    topic = mqtt_conf['topic']

    client = paho.Client()
    #client.username_pw_set(user,pwd)
    log.info('mqtt_client: connecting to mqtt broker...')
    client.connect(host, port)
    log.info('mqtt_client: connection successful')

    errCnt = 0
    
    try:
        log.info('mqtt_client: publishing payload to mqtt broker...')
        (rc, mid) = client.publish(topic, payload, qos=1)
        log.info("rc=%s, mid=%s" % (rc,mid) )
    except:
        errCnt += 1
        tb = traceback.format_exc()
        log.debug("!mqtt_client:\terrCnt: %s; last tb: %s" % (errCnt, tb))

     