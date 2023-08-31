from flask import Flask, render_template

app = Flask(__name__)

drinks_data = {
    'Wednesday': ['Espresso Martini', 'Margarita'],
    'Thursday': ['French 75', "Montepulciano D'Abruzzo"],
    'Friday': ['Untold Beer', 'Wine'],
    'Saturday': ['Beer', 'Wine'],
    'Sunday': ['Bloody Mary', 'Mimosa'],
}

food_data = {
    'Wednesday': {
        'Breakfast': ['eggs'],
        'Lunch': ['sandwich'],
        'Dinner': ['pickled pig eyes']
    },
    'Thursday': {
        'Breakfast': ['bagels'],
        'Lunch': ['fish'],
        'Dinner': ['steak']
    },
    'Friday': {
        'Breakfast': ['spinach'],
        'Lunch': ['onions'],
        'Dinner': ['chicken']
    },
    'Saturday': {
        'Breakfast': ['smoothies'],
        'Lunch': ['salads'],
        'Dinner': ['quinoa']
    },
    'Sunday': {
        'Breakfast': ['cereal'],
        'Lunch': ['alcohol'],
        'Dinner': ['pancakes']
    }
}

activities_data = {
    'Wednesday': ['Quiplash'],
    'Thursday': ['Football'],
    'Friday': ['Black Friday shopping'],
    'Saturday': ['Decorating house for Christmas'],
    'Sunday': ['Departure'],
}

room_arrangements_data = {
    'Nora and Richard': 'Front guest bedroom',
    'Molly': 'Back guest bedroom',
    'Maeve': "Murphy bed room (Alyssa's office)",
    'Cinnamon': "Pull-out couch (Aidan's office)",
    'Clare': 'Downstairs extra living room couch'
}

travel_arrangements_data = {
    'Nora and Richard': {
        'Arrival': 'Tuesday, by train to South Station',
        'Departure': 'Monday, by plane out of Logan',
        'means_of_transport': 'Ferry from Hingham Shipyard to Logan Airport'
    },
    'Molly': {
        'Arrival': 'No clue',
        'Departure': 'No clue',
        'means_of_transport': 'No clue'
    },
    'Maeve': {
        'Arrival': 'Cannot remember',
        'Departure': 'No clue',
        'means_of_transport': 'No clue'
    },
    'Cinnamon': {
        'Arrival': 'No clue',
        'Departure': 'No clue',
        'means_of_transport': 'No clue'
    },
    'Clare': {
        'Arrival': 'No clue',
        'Departure': 'No clue',
        'means_of_transport': 'No clue'
    }
}

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/travel')
def travel():
    return render_template('travel.html', travel_arrangements = travel_arrangements_data)

@app.route('/activities')
def activities():
    return render_template('activities.html', activities = activities_data)

@app.route('/drinks')
def drinks():
    return render_template('drinks.html', drinks = drinks_data)

@app.route('/food')
def food():
    return render_template('food.html', food = food_data)

@app.route('/room_arrangements')
def room_arrangements():
    return render_template('room_arrangements.html', room_arrangements = room_arrangements_data)

if __name__ == '__main__':
    app.run(debug=True)