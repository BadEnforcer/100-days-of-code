# iterating over things in pandas
import pandas
student_dict = {
    "students" : ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

df = pandas.DataFrame(student_dict)
# looping through

# basic method
# for (key, value) in df.items():
#     print(key)

# using built-in method in pandas
for (index, row) in df.iterrows():
    # print(index)
    # print(row)
    # print(row.students) # gives student names
    # print(row.score)  # gives score of everyone
    if row.students == "Lilly":
        print(row.score)
