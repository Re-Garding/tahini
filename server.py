from flask import Flask, render_template



app = Flask(__name__)
app.secret_key = "secretKEY"
app.app_context().push()

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/lodging')
def lodging():
    return render_template('lodging.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/FAQ')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run()