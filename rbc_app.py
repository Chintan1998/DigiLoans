from flask import Flask, render_template, redirect, url_for, request,url_for


app = Flask(__name__)
usr_pass = {"jane":"1234","Mary":"hell0","rndm":"smh"}

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    user = request.form['user']
    passw = request.form['pass']
    
    if(request.method == "POST"):
        if((user in usr_pass.keys())and (passw == usr_pass.get(user))):
            return render_template("404.html")
        else:
            return render_template("sign-up.html")
    else:
        return render_template('index.html')

app.route('/', methods=['POST'])
def x_form_post():
    user = request.form['usersignup']
    userlogin = request.form['userlogin']
    passlogin = request.form['passlogin']
    email = request.form['email']
    passw = request.form['passsignup']
    sinnum = request.form['sinnum']
    phnnum = request.form['phnnum']
    firstname = request.form['fname']
    lastname = request.form['lname']
    print(user,userlogin,passlogin,passw,email,sinnum,phnnum,firstname,lastname)
    if(request.method == "POST"):
        usr_pass[user] = [email.strip(),passw.strip(),sinnum.strip(),phnnum.strip(),firstname.strip(),lastname.strip()]
        return str(usr_pass)
    else:
        return render_template('sign-up.html')

if __name__ == '__main__':
    app.run()