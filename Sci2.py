#Name:Ethan Terrett
#Class: 5th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification
weight = int(input("Please enter your weight: "))
height = int(input("Please enter your height in inches: "))

# tried simplifying this below and it broke LOOOL

weight_more = weight * 703
less_answer = weight_more / height
BMI = less_answer / height
BMI = round(BMI, 1)

print(BMI)

if BMI >= 30:
    print("You are obese")
elif BMI >= 25 or BMI <= 29.9:
    print("You are overweight")
elif BMI >= 18.5 or BMI <= 25:
    print("Your weight is normal")
elif BMI <= 18.5:
    print("You are underweight")