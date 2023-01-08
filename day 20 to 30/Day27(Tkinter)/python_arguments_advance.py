# arguments have default value
# making function that can take unlimited positional arguments
def add(*args):
    print(sum(args))
    # for solution in args:
    #     print(solution)


# that * sign is very important
# those args will be in a tuple
add(1, 2, 3, 4, 5, 6, 7)  # returns 28


# refer to arguments by their name. not by their position in the tuple
# using ** kwargs
# "keywords" arguments
# this returns a dictionary
# def calculate(**kwargs):
#     print(kwargs)
#
#
# calculate(a=1, b=3, add=5)

class Snake:
    def __init__(self, **kwargs):  # or **kw
        self.model = kwargs["model"]  # or use kwargs.get("model")
        # that's it
        # using get will not give un an error but set itself to none


snake = Snake(model="GTR - 2.0", brand="Nissan")
