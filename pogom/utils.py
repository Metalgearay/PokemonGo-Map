#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getpass
import argparse
import re
import uuid
import os
import json
from datetime import datetime, timedelta

from . import config
from exceptions import APIKeyException


def parse_unicode(bytestring):
    decoded_string = bytestring.decode(sys.getfilesystemencoding())
    return decoded_string


def get_pokemon_name(pokemon_id):
    if not hasattr(get_pokemon_name, 'names'):
        file_path = os.path.join(
            config['ROOT_PATH'],
            config['LOCALES_DIR'],
            'pokemon.{}.json'.format(config['LOCALE']))

        with open(file_path, 'r') as f:
            get_pokemon_name.names = json.loads(f.read())

    return get_pokemon_name.names[str(pokemon_id)]

def load_credentials(filepath):
    with open(filepath+os.path.sep+'credentials.json') as file:
        creds = json.load(file)
        if not creds['gmaps_key']:
            raise APIKeyException(\
                "No Google Maps Javascript API key entered in credentials.json file!"
                " Please take a look at the wiki for instructions on how to generate this key,"
                " then add that key to the file!")
        return creds
