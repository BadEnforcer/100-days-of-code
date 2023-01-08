import requests
from flask import Flask, render_template


app = Flask(__name__)

blogs_data = requests.get('https://api.npoint.io/50c45d0b9582e301ea3b').json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs_data)


@app.route('/read-blog/<blog_id>')
def go_to_blog(blog_id):
    return render_template('post.html', contents=blogs_data[int(blog_id)])


if __name__ == "__main__":
    app.run(debug=True)
