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

# Маршрут для головної сторінки
@app.route('/')
def index():
    return render_template('index.html', title='Головна сторінка')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
і
