from flask import Flask, render_template, request

app = Flask(__name__)

# --- Dummy Database (Data Lists) ---
# Ye data hum HTML pages par bhejenge taaki page dynamic lage
WORKOUT_PLANS = [
    {"id": 1, "name": "HIIT Cardio", "level": "Beginner", "duration": "30 Mins", "cal": "300-400", "desc": "High Intensity Interval Training to burn fat fast."},
    {"id": 2, "name": "Muscle Building", "level": "Advanced", "duration": "60 Mins", "cal": "400-600", "desc": "Heavy compound lifts focusing on hypertrophy."},
    {"id": 3, "name": "Power Yoga", "level": "Intermediate", "duration": "45 Mins", "cal": "200-300", "desc": "Focus on flexibility, core strength and mental peace."},
    {"id": 4, "name": "CrossFit Challenge", "level": "Expert", "duration": "50 Mins", "cal": "600+", "desc": "Functional movements performed at high intensity."}
]

DIET_PLANS = {
    "veg": [
        "Breakfast: Oatmeal with almonds & banana",
        "Lunch: Brown Rice, Dal Tadka, Green Salad",
        "Snack: Greek Yogurt or Fruit Salad",
        "Dinner: Grilled Paneer with stir-fry veggies"
    ],
    "nonveg": [
        "Breakfast: 3 Boiled Eggs & Whole Wheat Toast",
        "Lunch: Grilled Chicken Breast with Quinoa",
        "Snack: Protein Shake or Boiled Chana",
        "Dinner: Baked Fish with Steamed Broccoli"
    ]
}

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/workouts')
def workouts():
    # Workouts ka data HTML file ko pass kar rahe hain
    return render_template('workouts.html', title="Workouts", plans=WORKOUT_PLANS)

@app.route('/diet')
def diet():
    return render_template('diet.html', title="Diet Plans", diets=DIET_PLANS)

@app.route('/bmi')
def bmi():
    return render_template('bmi.html', title="BMI Calculator")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact Us")

if __name__ == '__main__':
    app.run(debug=True)
