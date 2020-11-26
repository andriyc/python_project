from flask import Flask, jsonify, render_template

DEBUG_MODE = True;

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", message='CI/CD to DEV is working well !!! Powered by Jenkins!!!')


if __name__ == '__main__':
    app.run(debug=DEBUG_MODE)
