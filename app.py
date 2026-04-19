from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello! This is a simple Flask app running in Docker."

if __name__ == '__main__':
    # We set host to '0.0.0.0' so it's accessible outside the container
    app.run(debug=True, host='0.0.0.0', port=5000)
