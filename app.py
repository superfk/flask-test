from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello/<string:name>',  methods=['POST','GET'])
def get_name(name):
    return jsonify({'message':'hello {}'.format(name)})

if __name__=='__main__':
    app.run()