from flask import Flask,request,jsonify
from googlesearch import search

app = Flask(__name__) 

@app.route('/api',methods=['GET'])
def hello_world():
	d, links = {}, {}
	link = 1
	d['Query'] = str(request.args['Query'])
	for j in search(d['Query'], tld="co.in", num=3, stop=3, pause=2):
		links[f'{link}'] = j
		link += 1 
	return jsonify(links)


if __name__ == '__main__': 
	app.run()