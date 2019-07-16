from app import app
from flask import render_template, request
from app.models import model, formopener
from models.dad_jokes_api import getDadJoke

@app.route('/')
@app.route('/index')
def index():
    user = 'Margie'
    return render_template('index.html',user=user)

    
@app.route('/dadjoke', methods=['GET','POST'])
def bfast():
    if request.method == 'GET':
        return "Please use the form."
    else:
        # Flask method
        userdata=(request.form).to_dict(flat=True)
        joke=getDadJoke(userdata['search'])
        print(joke)
        return render_template('dadjoke.html',joke=joke)
    
    # return render_template('breakfast.html')
