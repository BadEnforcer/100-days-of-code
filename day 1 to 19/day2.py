# string
string = "hello"
print(string)

# print a specific letter (subscript)
print(string[4])

# integer
int_1 = 25
int_2 = 50
print(int_1 + int_2)

# you can use it to add comma
# ex - 342,654,896
part_1 = 342
part_2 = 654
part_3 = 896
print(str(part_1) + "," + str(part_2) + "," + str(part_3))

# computer will ignore these underscores!
nu = 342_654_896
print(nu)

# Float
f_var = 3.420
print(f_var)

# Boolean
# True or False

# find data type
print(type(nu))

# cool shit!!
print(70 + float("650.096"))  # it works

# rounding the numbers
# example = 2.956 to --------- 3
print(round(2.956))

# you can use precision
# ex- I want to round it for 2 decimal places
print(round(2.956, 2))  # this will give 2.96 EZ
# use comma inside the function

# we can use floor division
print(16 / 5)  # this gives 3.2 as float as the answer
print(16 // 5)  # this gives 3 as int

# some weird magic
result = 6 / 2  # 3
result /= 2  # 3/2 = 1.5
print(result)  # prints 1.5
# this can be used to do multiple ops
# #ex -
#   score = score + 1     #this can be replaced by
#   score += 1    #####both of these will do the same thing

# FStrings #used to simple things out. no need to change data types
score = 10
height = 1.8
isWinning = True
print(f"your score is {score}, you height is {height}, you are winning {isWinning}")
  