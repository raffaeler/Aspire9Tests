"""Webserver controllers"""
#import os
import logging
#from uuid import uuid4
from opentelemetry import metrics, trace
#from flask import Flask#, current_app
#from functools import partial

# __name__ = "controllers"


class WebServer:
    """Web server class"""
    def __init__(self, app):
        app.add_url_rule('/', view_func=self.hello, methods=['GET'])
        app.add_url_rule('/world', view_func=self.hello_world, methods=['GET'])
        app.add_url_rule('/moon', view_func=self.hello_moon, methods=['GET'])
        self.create_metrics()
        logging.getLogger(__name__).info("WebServer ctor")

    def create_metrics(self):
        """Create metrics"""
        self.meter = metrics.get_meter(__name__)
        self.counter = self.meter.create_counter(
            name="number_of_requests",
            unit="1",
            description="The number of http requests",
        )

        self.up_down = self.meter.create_up_down_counter(
            name="active_requests",
            unit="1",
            description="The number of active requests",
        )

    def hello(self):
        """Function"""
        try:
            self.up_down.add(1)

            with trace.get_tracer(__name__).start_as_current_span("hello"):
                logging.getLogger(__name__).info("request received!")

                self.counter.add(1)
                return '<h3>Hello!</h3><p><a href="/world">World</a></p>'
        finally:
            self.up_down.add(-1)


    # pylint: disable=unused-argument
    def hello_world(self):
        """Function returning Hello world"""
        logging.getLogger(__name__).info("hello_world")
        try:
            self.up_down.add(1)

            with trace.get_tracer(__name__).start_as_current_span("hello_world"):
                logging.getLogger(__name__).info("request received!")

                self.counter.add(1)
                return '<h3>Hello, World!</h3><p><a href="/moon">Moon</a></p>'
        finally:
            self.up_down.add(-1)

    def hello_moon(self):
        """Function returning Hello moon"""
        try:
            self.up_down.add(1)

            with trace.get_tracer(__name__).start_as_current_span("hello_moon"):
                logging.getLogger(__name__).info("request received!")

                self.counter.add(1)
                return '<h3>Hello, Moon!</h3><p><a href="/">Home</a></p>'
        finally:
            self.up_down.add(-1)
