import datetime as dt
""" # Weather Pridiction app """
weather = input("Enter your weather condation, sunny, cloudy, thunderston : ")

weather_input_space = weather.count(" ")
if weather_input_space >= 1:
    print("Please write without spaces")

if weather == "sunny":
    print("today is hot day")

if weather == "thunderston":
    print("today is rainy day")

if weather == "cloudy":
    print("today is outing day, but take umbrella with you")


""" # Subtotal with Sale tax """
total = 100
sale_tax_rate = 0.065
taxable = True

if taxable:
    print(f"Subtotal: ${total:,.2f}")

    sale_tax = total * sale_tax_rate
    print(f"Sale Tax: ${sale_tax:.2f}")

    total = total + sale_tax
    print(f"Total   : ${total:.2f}")

if taxable == False:
    print("Please Pay SalesTax ")


"""  # Greeting Message with current time """

now = dt.datetime.now()


if now.hour < 12 and now.hourhour >= 4:
    print("Good Morning")
elif now.hour >= 12 and now.hour <= 18:
    print("Good Afternoon")
else:
    print("Good Night")

print("I hope you are doing well")


"""  # Baverage  provide according to Age  """

user_age = int(input("Enter your Age "))

if user_age < 21:
    baverage = "Milk"
elif user_age >= 21 and user_age < 80:
    baverage = "Beer"
else:
    baverage = "Prune Juice"

print(f"Have a {baverage}")
