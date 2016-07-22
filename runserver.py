#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser
import os
import logging
import subprocess
from threading import Thread
from pogom import config
from pogom.app import Pogom
from pogom.utils import  load_credentials
from pogom.search import search_loop
from pogom.models import create_tables, Pokemon, Pokestop, Gym

from pogom.pgoapi.utilities import get_pos_by_name

log = logging.getLogger(__name__)


def start_locator_thread(auth,username,password,location,steps):
    search_thread=Thread(target=search_loop, args=(auth,username,password,location,steps,))
    search_thread.daemon = True
    search_thread.name = 'search_thread'
    search_thread.start()

def run(auth,username,password,location,steps):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(module)11s] [%(levelname)7s] %(message)s')
    logging.getLogger("peewee").setLevel(logging.INFO)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("pogom.pgoapi.pgoapi").setLevel(logging.WARNING)
    logging.getLogger("pogom.pgoapi.rpc_api").setLevel(logging.INFO)
    create_tables()
    url='http://localhost:5000'
    webbrowser.open_new(url)
    position = get_pos_by_name(location)
    log.info('Parsed location is: {:.4f}/{:.4f}/{:.4f} (lat/lng/alt)'.
             format(*position))

    config['ORIGINAL_LATITUDE'] = position[0]
    config['ORIGINAL_LONGITUDE'] = position[1]
    config['LOCALE'] = "en"
    start_locator_thread(auth,username,password,location,steps)


    app = Pogom(__name__)
    config['ROOT_PATH'] = app.root_path
    debug=False
    host='127.0.0.1'
    port=5000
    config['GMAPS_KEY'] = load_credentials(os.path.dirname(os.path.realpath(__file__)))['gmaps_key']
    app.run(threaded=True, debug=debug, host=host, port=port)
