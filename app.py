from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'CD to DEV is working well !!!'

if __name__ == '__main__':
    app.run()
