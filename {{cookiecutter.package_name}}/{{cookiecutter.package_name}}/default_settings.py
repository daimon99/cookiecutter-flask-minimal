# coding: utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False  # make sure DEBUG is off unless enabled explicitly otherwise
LOG_DIR = os.path.join(BASE_DIR, 'logs')  # create log files in current working directory

if not os.path.exists(BASE_DIR):
  os.mkdir(BASE_DIR)
