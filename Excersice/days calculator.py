# 🚨 Don't change the code below 👇
age = input("What is you current Age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
base_year = int(input("How many years to assume for? \n\n"))
years_left = base_year - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
result = f"You have {days_left} Days, {weeks_left} weeks, {months_left} months left Assuming you will live for {base_year} Years"
print(result)
