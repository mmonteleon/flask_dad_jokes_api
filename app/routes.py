from app import app
from flask import render_template, request
from app.models import model, formopener
from app.models.model import getDadJoke

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

    
@app.route('/dadjoke', methods=['GET','POST'])
def dadjoke():
    if request.method == 'GET':
        return "Please use the form."
    else:
        userdata=(request.form).to_dict()
        joke=getDadJoke(userdata['search'])
        return render_template('dadjoke.html',joke=joke)

