"""Service exposed via HTTP"""

#import os
#import sys
#import argparse
import logging
#from opentelemetry import metrics
from opentelemetry import trace
from flask import Flask
from controllers import WebServer

logging.basicConfig()
logging.getLogger().setLevel(logging.NOTSET)
logging.getLogger().info("Starting the application")

# demo on using the trace API
with trace.get_tracer("my.tracer").start_as_current_span("foo"):
    with trace.get_tracer("my.tracer").start_as_current_span("bar"):
        print("baz")

logging.getLogger(__name__).info("Starting the web server")
app = Flask(__name__)
server = WebServer(app)
app.run()
