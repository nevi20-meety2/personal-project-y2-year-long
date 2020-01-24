from flask import Flask,render_template,url_for,request,redirect
from database import *

app = Flask(__name__)

@app.route('/')
def open():
    return render_template("openpage.html")

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        add_user(request.form['firstname'],request.form['lastname'],
            request.form['username'],request.form['password'],
            request.form['media'],request.form['song'],
            request.form['member'],request.form['album'],
            request.form['opinion'])
        return redirect(url_for('log_in'))

@app.route('/log_in', methods=["GET","POST"])
def log_in():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if checkUser(request.form['username'],request.form['password']):
            return redirect(url_for('home'))
        else:
            return render_template('login.html')

@app.route('/home')
def home():
     return render_template('homepage.html')

@app.route('/harrystyles')
def harry():
     return render_template('harry.html')

@app.route('/liampayne')
def liam():
     return render_template('liam.html')

@app.route('/profile')
def profile():
     return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)