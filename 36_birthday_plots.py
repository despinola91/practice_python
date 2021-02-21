# Exercise: https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

# This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.
# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in! 
# Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday 
# JSON file. Just parse out the months (if you don’t know how, I suggest looking at the previous exercise or its solution) 
# and draw your histogram.

# If you are using a purely web-based interface for coding, this exercise won’t work for you, 
# since it requires installing the bokeh Python package. Now might be a good time to install Python on your own computer.

from bokeh.plotting import figure, show, output_file
from collections import Counter as c
import json

fileName = "34_birthdays.json"

def get_birthdays():
    global birthdays
    with open(fileName, "r") as f:
        birthdays = json.load(f)
    return birthdays

def get_months_counter():
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
    return result


def show_chart(x, y):
    output_file("36_plot.html")

    x_categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dic"]
    
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)

    show(p)

def run():
    result = get_months_counter()

    x = list(result.keys())
    y = list(result.values())

    show_chart(x, y)

if __name__ == "__main__":
    run()