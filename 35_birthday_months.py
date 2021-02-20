# Exercise:
# https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
# 
# This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

# In the previous exercise we saved information about famous scientists’ names and birthdays to disk. 
# In this exercise, load that JSON file from disk, extract the months of all the birthdays, 
# and count how many scientists have a birthday in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }

import json
from collections import Counter as c
fileName = "34_birthdays.json"

def get_birthdays():
    global birthdays
    with open(fileName, "r") as f:
        birthdays = json.load(f)
    return birthdays


def show_months_counter():
    months = list()
    birthdays = get_birthdays()

    for value in birthdays.values(): 
        month_number = value[:2]
        if month_number == "01":
            months.append("Jan")
        elif month_number == "02":
            months.append("Feb")
        elif month_number == "03":
            months.append("Mar")
        elif month_number == "04":
            months.append("Apr")
        elif month_number == "05":
            months.append("May")
        elif month_number == "06":
            months.append("Jun")
        elif month_number == "07":
            months.append("Jul")
        elif month_number == "08":
            months.append("Aug")
        elif month_number == "09":
            months.append("Sep")
        elif month_number == "10":
            months.append("Oct")
        elif month_number == "11":
            months.append("Nov")
        elif month_number == "12":
            months.append("Dec")
    
    result = c(months)
    print(json.dumps(result, sort_keys=False, indent=4))
    

def run():
    show_months_counter()

if __name__ == "__main__":
    run()