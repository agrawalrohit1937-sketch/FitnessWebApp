// --- Mobile Menu Toggle ---
const mobileMenu = document.getElementById('mobile-menu');
const navList = document.querySelector('.nav-menu');

if(mobileMenu){
    mobileMenu.addEventListener('click', () => {
        navList.classList.toggle('active');
    });
}

// --- BMI Calculator Logic ---
function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const resultDiv = document.getElementById('result');
    const bmiValue = document.getElementById('bmi-value');
    const bmiStatus = document.getElementById('bmi-status');

    if (isNaN(weight) || isNaN(height) || height <= 0 || weight <= 0) {
        alert("Please enter valid positive numbers!");
        return;
    }

    // Convert cm to m
    const heightInMeters = height / 100;
    const bmi = (weight / (heightInMeters * heightInMeters)).toFixed(1);

    // Show Result Div
    resultDiv.classList.add('show');
    bmiValue.innerText = bmi;

    let status = "";
    let color = "";

    if (bmi < 18.5) {
        status = "Underweight 🔵";
        color = "#3498db";
    } else if (bmi >= 18.5 && bmi < 24.9) {
        status = "Healthy Weight 🟢";
        color = "#2ecc71";
    } else if (bmi >= 25 && bmi < 29.9) {
        status = "Overweight 🟠";
        color = "#f39c12";
    } else {
        status = "Obese 🔴";
        color = "#e74c3c";
    }

    bmiStatus.innerText = status;
    bmiStatus.style.color = color;
}
