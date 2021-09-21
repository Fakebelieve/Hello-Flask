from flask import Flask
import random
app = Flask('app')

@app.route('/')
def hello_world():
	x = random.randint(1,10)
	return '<h1>Hello, World'+str(x)+'!</h1>'


app.run(host='0.0.0.0', port=8080)