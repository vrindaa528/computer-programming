#Program: Calculate BMI and Categorize
#Question: Write a function to calculate BMI and categorize the result based on BMI value.

Solution:

python
def calculate_bmi(weight, height):
    """
    Calculate BMI given weight in kilograms and height in meters.
    """
    return weight / (height ** 2)

def categorize_bmi(bmi):
    """
    Categorize BMI value into different classes.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")

if __name__ 
