"""gunicorn configuration"""
import os

bind = "0.0.0.0:8111"
os.environ["RAF"] = "raf"
