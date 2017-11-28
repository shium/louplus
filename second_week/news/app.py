#?/usr/bin/env python3

from flask import Flask, render_template
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOADI'] = True
files_path = '/home/shiyanlou/files/'

@app.route('/')
def index():
    title = []
    filename = os.listdir(files_path)
    for f in filename:
        p = files_path + f
        with open(p,'r') as f:
            data = json.load(f)
            title.append(data['title'])
    return render_template('index.html', title = title)

@app.route('/files/<filename>')
def file(filename):
    try:
        with open(files_path+filename+'.json','r') as f:
            data = json.load(f)
            return render_template('file.html', data = data)
    except FileNotFoundError:
        return render_template('404.html')
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
