import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
randint = random.randint(0, 1)
if randint == 1:
    print('Heads')
elif randint == 0:
    print("Tails")
