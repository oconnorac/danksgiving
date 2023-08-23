from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/room_arrangements')
def room_arrangements():
    return render_template('room_arrangements.html')

if __name__ == '__main__':
    app.run(debug=True)