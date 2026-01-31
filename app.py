from flask import Flask, render_template

app = Flask(__name__)

# --- Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')

@app.route('/bmi')
def bmi():
    return render_template('bmi.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- Main Entry Point ---
if __name__ == '__main__':
    # Debug=True helps during development to see errors instantly
    app.run(debug=True)