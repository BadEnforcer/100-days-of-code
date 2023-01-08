from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

time = datetime.now()


@app.route('/')
def home():
    player_name = "Raj"
    year = time.year
    return render_template("index.html", p=player_name, copyright_year=year)


@app.route('/guess/')
def api():
    dgs = requests.get('https://status.digitalocean.com/api/v2/status.json').json()['status']['description']
    return render_template('status.html', status=dgs)


@app.route('/blog/<num>/')
def av(num):
    print(num)
    raw_data = requests.get('https://api.npoint.io/50c45d0b9582e301ea3b').json()
    # return render_template('blog.html')
    return render_template('blog.html', blog_post=raw_data[int(num)])


if __name__ == "__main__":
    app.run(debug=True)
