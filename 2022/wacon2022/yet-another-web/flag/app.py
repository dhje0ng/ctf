from flask import Flask

app = Flask(__name__)

@app.route('/')
def flag():
    return 'WACon{FAKE_FAKE}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=31337)