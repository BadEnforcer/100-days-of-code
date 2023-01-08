# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_path = "./Input/Names/invited_names.txt"
template = "./Input/Letters/starting_letter.txt"
output_folder = "./Output/ReadyToSend/"

# grab the name
with open(name_path, "r") as file:
    names = file.readlines()

# grab the letter
with open(template, mode="r") as file:
    letter_content = file.readlines()
    # print(letter_content[0])

for name in names:
    True_name = name.strip("\n")
    letter_content[0] = "Dear " + True_name + "," + "\n"
    file_path = output_folder + True_name + ".txt"
    with open(file_path, mode="w") as file:
        for i in letter_content:
            file.write(i)
# we can just use strip(). it also works to remove newline.
