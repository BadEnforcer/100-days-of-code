# functions with output
def format_name(f_name, l_name):
    """hello"""
    # print name in title case
    if f_name or l_name == "":
        return "Not valid input. Please restart."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"  # this will make the function call block to the output


formatted_string = format_name(f_name="Raj", l_name="dwivedi")
print(formatted_string)

# what if we have more than return statements
# code written below return statement will not run
# if we put return in loops or if statements to break it and tell a custom message. see example

# doc strings
# after declaring a var u need to and three " marks and type inbetween