from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'CI/CD to DEV is working well !!! Powered by Jenkins.'


if __name__ == '__main__':
    app.run()
