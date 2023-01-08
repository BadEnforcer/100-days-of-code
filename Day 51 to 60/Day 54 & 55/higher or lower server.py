import random

from flask import Flask

app = Flask(__name__)

random_n = random.randint(0, 9)


@app.route('/')
def guess():
    return "<h1>Guess the number between: 1-9</h1>" \
           "<br>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"




@app.route('/<number>')
def check(number):
    if int(number) == random_n:
        return "<h1>You GOT IT!!!</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

    if int(number) > random_n:
        return "<h1>Too High, Try Again.</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"

    if int(number) < random_n:
        return "<h1>Too Low, Try Again.</h1>" \
               "<br>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


app.run()
