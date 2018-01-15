import random
import pandas as pd
import os
import time
import json

from app.app import app
from flask import request, render_template, session, url_for, redirect

@app.template_filter('autoversion')
def autoversion_filter(filename):
  # determining fullpath might be project specific
  fullpath = os.path.join('some_app/', filename[1:])
  try:
      timestamp = str(os.path.getmtime(fullpath))
  except OSError:
      return filename
  newfilename = "{0}?v={1}".format(filename, timestamp)
  return newfilename

# Views
@app.route('/')
def main():
    return render_template('/index.jade')
