#Program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value: under 18.5 they are underweight, over 18.5 but below 25 they have a normal weight. 
# If they are over 25 but below 30 they are slightly overweight, over 30 but below 35 they are obese, above 35 they are clinically obese.
#Warning: the result should be rounded to the nearest whole number. 
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m).

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = int(weight)/ float(height) ** 2

round_bmi = round(bmi)

if round_bmi < 18.5:
  print(f"Your BMI is {round_bmi}, you are underweight.")
elif round_bmi <= 25:
  print(f"Your BMI is {round_bmi}, you have a normal weight.")
elif round_bmi <= 30:
  print(f"Your BMI is {round_bmi}, you are slightly overweight.")
elif round_bmi <= 35:
  print(f"Your BMI is {round_bmi}, you are obese.")
else:
  print(f"Your BMI is round_bmi, you are clinically obese.")