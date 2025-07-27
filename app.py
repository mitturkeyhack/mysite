from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "gizli-anahtar"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
def profile():
    if not session.get("user"):
        return redirect(url_for("login"))
    return render_template('profile.html', user=session["user"])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        session['user'] = email
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
