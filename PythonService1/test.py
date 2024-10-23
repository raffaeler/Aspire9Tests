"""Service exposed via HTTP"""

import os
import flask

print("Start1")

print("Start2")
app = flask.Flask(__name__)
print("Start3")

@app.route('/', methods=['GET'])
def hello_world():
    """Function returning Hello world"""
    return 'Hello, What???'

print("Start4")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8111))
    print("Start5")
    app.run(host='0.0.0.0', port=port)
