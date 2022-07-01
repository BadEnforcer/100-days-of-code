# with open("weather_data.csv")as data_file:
#     content = data_file.readlines()

# use inbuilt library

# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)  # returns a csv object
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(row[1])
#     print(temps)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# # convert to dic
# # data_dict = data.to_dict()
#
# # convert series to list
# temp_list = data["temp"].tolist()
#
# # task : find avg temp
# avg = sum(temp_list) / len(temp_list)
# print(avg)
#
# # we can use pandas mean function instead
# print(data["temp"].mean())
# # print max value
# print(data["temp"].max())
#
# # we can use these lines instead
# # condition = data["condition"]
# print(data.condition)  # it works  NOTE: it's case-sensitive
#
# # get data from a row
# day_data = data[data.day == "Monday"]  # we call the database, call the days' column. then we grab the "Monday" Row.
# print(day_data)
#
# # print row with max temp
# print(data[data.temp == data.temp.max()])

# # we can use it like this also
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)  # Celsius to Fahrenheit

# how to create a dataFrame from Scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
# print it or make it into a file. for ex -
data.to_csv("./new_csv.csv")
