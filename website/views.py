from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/') # home search route
def home():
    return "<h1>HOME PLACEHOLDER</h1>" # return some simple html

@views.route('search') # search page 
def search():
    return "<h1>SEARCH PAGE PLACEHOLDER</h1>"

@views.route('profile')
def profile():
    return "<h1>PROFILE PLACEHOLDER</h1>"