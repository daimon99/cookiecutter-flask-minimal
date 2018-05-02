import os
from flask import Flask
from curlbin import log_config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
log_config.set_logging(os.path.join(BASE_DIR, 'logs'))

app = Flask('curlbin')
app.config.from_object('curlbin.default_settings')

import dotenv

dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))

import curlbin.views  # Must be loaded at last
