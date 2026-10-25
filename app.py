from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Головна сторінка сайту"

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакти')

if __name__ == '__main__':
    app.run(debug=True)