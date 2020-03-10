from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    main_html = '''
    <input type='text' placeholder='你的姓名'>
    <button id='confirmBtn'>確定</button>
    '''
    return main_html

@app.route('/test')
def test():
    return 'This is Test'

if __name__=='__main__':
    app.run()