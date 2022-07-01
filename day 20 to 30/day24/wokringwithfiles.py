# file = open("my-file.txt")  # open file . read inside it. get the content. print it.
# contents = file.read()
# print(contents)
# # file.close()  # it uses resources if left open.
#

# instead we use this method for easily closing files
with open("my-file.txt") as file:
    contents = file.read()
    print(contents)  # file will be automatically closed

# write to file
with open("my-file.txt", mode="a")as file:   # we need to open the file in write mode or it wont work.
    file.write("\nhellhole boi")
    print(contents)

    # "w" will delete everything. use "a" for append
    # in write mode if a file does not exist. it will create it.
