from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'gizli-anahtar'

@app.route('/')
def home():
    return render_template('index.html', title="Ana Sayfa")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['email'] = request.form['email']
        return redirect(url_for('profile'))
    return render_template('login.html', title="Giriş")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', title="Profil")

@app.route('/about')
def about():
    return render_template('about.html', title="Hakkında")

if __name__ == '__main__':
    app.run()
