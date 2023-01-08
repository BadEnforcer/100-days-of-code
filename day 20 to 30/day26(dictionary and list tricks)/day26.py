# # list comprehension
#
# # old method
# numbers = [1, 2, 3]
# # new_list = []
# # for solution in numbers:
# #     add_1 = solution + 1
# #     new_list.append(add_1)
#
# # new method
#
# # new_list = [new_item for item in list]  <<<< # SYNTAX
# #
# new_list = [solution + 1 for solution in numbers]
# # new list = [{actual program}, for {what do u want to call the numbers in the list you're going through} in
# # {the list you're going through}.
#
#
# # this is not restricted to list. it can be used for strings, tuple, range also.
# # string
# name = "Raj"
# new_name = [letter for letter in name]
#
# # range
# # range = range(1,5)
# new_range = [num * 2 for num in range]

# conditional list comprehension
# syntax >>> new_list =[new_item for item in list if test]
# only run the code if test passes

# example
# names = ["alex", "Beth", "Arthur", "Dave", "Franklin"]
# short_names = [name for name in names if len(name) <= 4]
# upper_case_names = [name.upper() for name in names if len(name) > 4]




