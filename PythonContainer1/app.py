"""Service exposed via HTTP"""

import os
import logging
from uuid import uuid4
from opentelemetry import metrics, trace
import flask

os.environ["MyGuid"] = os.environ['HOME'] + '_' + str(uuid4())

logging.basicConfig()
logging.getLogger().setLevel(logging.NOTSET)
logging.getLogger().info("Starting the application")

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

up_down = meter.create_up_down_counter(
    name="active_requests",
    unit="1",
    description="The number of active requests",
)

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """Function returning Hello world"""
    try:
        up_down.add(1)

        with trace.get_tracer("my.tracer").start_as_current_span("hello_world"):
            logging.getLogger(__name__).info("request received!")

            counter.add(1)
            return 'Hello, What???'
    finally:
        up_down.add(-1)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8111))
    app.run(host='0.0.0.0', port=port)
