from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/not-hello')
def not_hello():
    return 'Hi, Docker!'

@app.route('/good-bye')
def good_bye():
    return 'Bye, Docker!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5005)

