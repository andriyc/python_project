from flask import Flask, jsonify, render_template
import configparser

app = Flask(__name__)


def init_globals() -> configparser:
    config = configparser.ConfigParser()
    config.read('settings/config.ini')
    return config


config = init_globals()


@app.route('/')
def index():
    return render_template("index.html", message=config['MESSAGE']['CI_CD_WORKING'])


if __name__ == '__main__':
    app.run(debug=(config['APP']['DEBUG_MODE'].lower() == 'true'))
