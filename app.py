import re

from itertools import count


from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import requests
import base64

app = Flask(__name__, static_folder='static2')

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		
		inp_url = request.form['PostInput']
		
		if inp_url == '':
			return render_template('index.html', status='error')
		
		base_url = 'https://www.instagram.com/p/'
		
		m = inp_url.split('/')
		for i in range(len(m)):
			if m[i] == 'p':
				code = m[i+1]
				break


		url_t = base_url + code + '/media/?size=t'
		url_m = base_url + code + '/media/?size=m'
		url_l = base_url + code + '/media/?size=l'

		req_m = requests.get(url_m)
		req_l = requests.get(url_l)
		
		if req_m.status_code == requests.codes.ok:
			return render_template('index.html', img_big=req_l.url, img_small=req_m.url, status='success')
		else:
			return render_template('index.html', status='error')

	return render_template('index.html')    


@app.route('/about')
def about(name=None):
	return render_template('about.html', name=name)    

if __name__ == '__main__':
	app.run()
