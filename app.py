from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running much better. And even more better!!!'

if __name__ == '__main__':
    app.run()
