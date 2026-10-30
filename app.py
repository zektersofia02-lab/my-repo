from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html', title='Головна сторінка')
=======
    return render_template('index.html', title='Головна')

@app.route('/about')
def about():
    return render_template('about.html', title='Про нас')

@app.route('/services')
def services():
    return render_template('services.html', title='Послуги')
>>>>>>> 17af525bacdb8aab5b329a7f54cb08389b6f0a48

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакти')

if __name__ == '__main__':
<<<<<<< HEAD
   app.run(debug=True)
=======
<<<<<<< HEAD
    app.run(debug=True, port=5000)
=======
    app.run(debug=True)

# Маршрут для головної сторінки
@app.route('/')
def index():
    return render_template('index.html', title='Головна сторінка')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
і
>>>>>>> 081ac132424e2e118e44c12d9a404ca22cc6660b
>>>>>>> 17af525bacdb8aab5b329a7f54cb08389b6f0a48
