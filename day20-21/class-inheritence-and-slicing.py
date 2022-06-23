class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale, exhale")


# example -
class Fish(Animal):
    def __init__(self):
        super().__init__()

    # super is not required but recommended for easier maintenance
    def swim(self):
        print("Swimming in water")

    # we pass the class in the (). # it's also know as super CLASS
    # then use super command to get the attributes of the passed class
    def breathe(self):
        super().breathe()  # what is going on? we are adding more things to breathing method but first
        # we are calling the breathing function from super class so the base functions is also included,
        # and we don't have to type it again
        print("doing this underwater")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(f"eyes = {nemo.eyes}")

# slicing
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[2:5:2])
# will print things after number 2 to number 5. but will skip every 2nd element
# ex - above code prints-  [3,5]
print(numbers[::2])
# go from start to end skipping every 2nd item
# to go in reverse
print(numbers[::-1])
