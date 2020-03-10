from flask import Flask, jsonify, request, render_template, url_for

app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello/<string:name>',  methods=['POST','GET'])
def get_name(name):
    return jsonify({'message':'Hello {}, You receive a smile'.format(name)})

if __name__=='__main__':
    app.run()