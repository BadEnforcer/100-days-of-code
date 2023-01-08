import pandas
# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
result = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

is_true = True
while is_true:
    try:
        word = str(input("Enter the word: ").upper())
        for alphabet in word:
            print(f"{alphabet}: {result[alphabet]}")
            is_true = False
    except KeyError:
        print("Alphabets only.")
