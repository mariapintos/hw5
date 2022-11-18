# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == "red":
        return "stop"
    if light == "green":
        return "go"
    if light == "yellow":
        return "wait"
    else:
        raise Exception('Undefined instruction for color: <light>') 

print(car_at_light("red"))


# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

def read_data(file_name):
    try:
        f=open(file_name)
    except IOError:
        print('File not accessible')

read_data("data.csv")

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.

my_list=["18-01-1998","25-02-2022", "03-03-2005"]
import pandas as pd
def get_day_month_year(dates_list):
    dates_list=pd.DatetimeIndex(dates_list)
    def dict_day_month_year(datetime):
        my_dictionnary = {"day": datetime.day,
                                 "month": datetime.month,
                                 "year": datetime.year}
        return my_dictionnary
    return pd.DataFrame(data=list(map(dict_day_month_year, dates_list)))

print(get_day_month_year(my_list))