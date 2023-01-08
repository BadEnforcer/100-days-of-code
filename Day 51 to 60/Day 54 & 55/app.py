from flask import Flask

app = Flask(__name__)


# text decorators
def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_italic(function):
    def wrapper():
        return f'<em>{function()}</em>'

    return wrapper


def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'

    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@make_bold
def say_bye():
    return "BYEE"


@app.route('/users/<name>')
def greet(name):
    return f"Hello {name}"


app.run(debug=True)

# def delay_deco(function):
#     print("running inside delay deco")
#     function()
#
#
# @delay_deco
# def say_hi():
#     print("hi!")
