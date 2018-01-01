print('''
	~~~~~~ Welcome to Codeilm ~~~~~~
			**********
	''')
name = input("What's your name? ")
print("Hi", name, "Myself tweety")
print("If I am angry i'll call you ", name.upper())
print("If I need something i'll call you ", name.lower())
print("Or else i'll call you ", name.title())

age = int(input("What's your age? "))
number_of_days = age * 365
number_of_hours = number_of_days * 24
number_of_minutes = number_of_hours * 60
number_of_seconds = number_of_minutes * 60

print("Do you know?", end=" ")
print("You have lived for", number_of_days, " days", end=" ")
print("You have lived for", number_of_hours, " hours", end=" ")
print("You have lived for", number_of_minutes, " minutes", end=" ")
print("You have lived for", number_of_seconds, " seconds")


