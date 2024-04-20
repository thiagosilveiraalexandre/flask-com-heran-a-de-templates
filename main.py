from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Redirecionando a rota inicial para a página inicial
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

