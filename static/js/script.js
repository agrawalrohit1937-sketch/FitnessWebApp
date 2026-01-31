function calculateBMI() {
    let weight = document.getElementById('weight').value;
    let height = document.getElementById('height').value;
    let resultDiv = document.getElementById('result');

    if (weight === "" || height === "") {
        resultDiv.innerHTML = "Please enter valid values!";
        resultDiv.style.color = "red";
        return;
    }

    // Convert height from cm to meters
    let heightInMeters = height / 100;
    
    // Calculate BMI
    let bmi = (weight / (heightInMeters * heightInMeters)).toFixed(2);
    
    let message = "";
    if (bmi < 18.5) message = "Underweight";
    else if (bmi >= 18.5 && bmi < 24.9) message = "Normal Weight";
    else if (bmi >= 25 && bmi < 29.9) message = "Overweight";
    else message = "Obese";

    resultDiv.innerHTML = `Your BMI is <span>${bmi}</span> (${message})`;
    resultDiv.style.color = "#00d4ff";
}