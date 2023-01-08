with open("file1.txt") as file:
    temp = file.readlines()
    file_1 = [number.strip() for number in temp]

with open("file2.txt") as file:
    temp = file.readlines()
    file_2 = [number.strip() for number in temp]


result = [number for number in file_1 if number in file_2]

# Write your code above 👆

print(result)
