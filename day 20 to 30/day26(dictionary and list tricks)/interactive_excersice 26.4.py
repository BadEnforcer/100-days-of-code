sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words = sentence.split()
# syntax help " result ={new_key:new_value for item in sentence.split()}
result = {word: len(word) for word in words}

print(result)
