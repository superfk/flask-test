from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>hello Flask</h1>'

@app.route('/test')
def test():
    return 'This is Test'

if __name__=='__main__':
    app.run()