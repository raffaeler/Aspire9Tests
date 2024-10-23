"""Service exposed via HTTP"""

import os
import logging
#from uuid import uuid4
from opentelemetry import metrics, trace
import flask

logging.basicConfig()
logging.getLogger().setLevel(logging.NOTSET)
logging.getLogger().info("Starting the application")

print("Start1")

# using the trace API
with trace.get_tracer("my.tracer").start_as_current_span("foo"):
    with trace.get_tracer("my.tracer").start_as_current_span("bar"):
        print("baz")


# create a counter using metrics
meter = metrics.get_meter(__name__)
counter = meter.create_counter(
    name="number_of_requests",
    unit="1",
    description="The number of http requests",
)

print("Start2")
app = flask.Flask(__name__)
print("Start3")

@app.route('/', methods=['GET'])
def hello_world():
    """Function returning Hello world"""
    with trace.get_tracer("my.tracer").start_as_current_span("hello_world"):
        logging.getLogger(__name__).info("request received!")

        counter.add(1)
        return 'Hello, What???'

print("Start4")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8111))
    print("Start5")
    logging.getLogger().info("Starting5")
    app.run(host='0.0.0.0', port=port)
