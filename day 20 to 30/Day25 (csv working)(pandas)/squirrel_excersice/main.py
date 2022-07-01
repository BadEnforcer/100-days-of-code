import pandas

data = pandas.read_csv("squirrel_data.csv")
Fur = data["Primary Fur Color"]
Gray = 0
Cinnamon = 0
Black = 0
Red = 0
for color in Fur:
    if color == "Gray":
        Gray += 1
    if color == "Cinnamon":
        Cinnamon += 1
    if color == "Red":
        Red += 1
    if color == "Black":
        Black += 1

count_dict = {
    "Color": ["Black", "Gray", "Red", "Cinnamon"],
    "Number of squirrels": [Black, Gray, Red, Cinnamon]
}

count_data = pandas.DataFrame(count_dict)
count_data.to_csv("./exported_number.csv")

# alternative method
Gray_count = len(data[data["Primary Fur Color"] == "Gray"])
print(Gray_count)