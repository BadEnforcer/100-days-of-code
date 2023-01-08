import pandas

DATA_LOCATION = "50_states.csv"
data = pandas.read_csv(DATA_LOCATION)
image = "blank_states_img.gif"
# we can use .item to grab the data from series too ex - data.state.item()


ALL_STATES = {"states": []}  # we can just use it as a list. but it might be good idea to add a header
for state in data.state:
    ALL_STATES["states"].append(state)

print(ALL_STATES)
