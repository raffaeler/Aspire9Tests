"""gunicorn configuration"""
import os

# pylint: disable = invalid-name
bind = "0.0.0.0:8111"
os.environ["RAF"] = "raf"
