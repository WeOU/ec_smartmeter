# -*- coding: utf-8 -*-
"""
This is a simple Flask app that query the meter and returns the values in a JSON format
"""

from flask import Flask
from test_meter import query_data
import json

app = Flask(__name__)


@app.route('/')
def index():
    """
    Home handler
    """
    
    return 'hello'


@app.route('/A', methods=['GET'])
def queryA():
    """
    Query meter in mode A
    """
    
    response = query_data()
    
    # Don't forget to return the response.
    return json.dumps(response)


# Run the app.
if __name__ == '__main__':
    app.run(debug=True, port=8080, host= '0.0.0.0')