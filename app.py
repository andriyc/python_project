import os
import sys
from flask import Flask, jsonify, render_template
from settings.config import project_properties

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message=project_properties.get('MESSAGE', 'CI_CD_WORKING'))


if __name__ == '__main__':
    app.run(debug=project_properties.is_true('APP', 'DEBUG_MODE'))
