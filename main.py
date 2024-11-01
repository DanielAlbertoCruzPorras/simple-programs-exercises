from time import localtime

# Get current date
current_time = localtime()
current_day = current_time.tm_mday
current_month = current_time.tm_mon
current_year = current_time.tm_year

day_of_birth = int(input("Enter your day of birth: "))
month_of_birth = int(input("Enter your month of birth: "))
year_of_birth = int(input("Enter your year of birth: "))

# Calculate initial age difference
age = current_year - year_of_birth

# Check if the birthday has already passed this year
if (month_of_birth > current_month) or (month_of_birth == current_month and day_of_birth > current_day):
    age -= 1

print(f"You are {age} years old.")

