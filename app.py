from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return render_template('main.html')

@app.route('/trend',methods=['GET'])
def trend():
	return render_template('trend.html')

@app.route('/models',methods=['GET'])
def models():
	return render_template('model.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
