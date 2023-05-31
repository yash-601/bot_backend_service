from flask import Flask,request,jsonify
from googlesearch import search

app = Flask(__name__) 

@app.route('/api',methods=['GET'])
def hello_world():
	d, links = {}, {}
	link = 1
	query = request.args['Query'].split(",")
	d['Query'] = query[0] + query[1]
	for j in search(d['Query'], tld="co.in", num=2, stop=2, pause=2):
		links[f'{link}'] = j
		link += 1 
	d['Query'] = query[0] + query[2]
	for j in search(d['Query'], tld="co.in", num=2, stop=2, pause=2):
		links[f'{link}'] = j
		link += 1 
	d['Query'] = query[0] + query[3]
	for j in search(d['Query'], tld="co.in", num=1, stop=1, pause=2):
		links[f'{link}'] = j
		link += 1 
	return jsonify(links)


if __name__ == '__main__': 
	app.run()