from flask import Flask, render_template
from requests import get

# NOTE: Fully functional blog was created as a personal project

app = Flask(__name__)

blog_posts_endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
blog_posts_data = get(url=blog_posts_endpoint).json()



@app.route('/')
@app.route('/index.html')
def homepage():
    return render_template('index.html', blogs=blog_posts_data)


@app.route('/about.html')
def about_page():
    return render_template('about.html')


@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')


@app.route("/view_post/<post_id>")
def go_to_blog(post_id):
    return render_template('post.html', data=blog_posts_data[int(post_id) - 1])



app.run(debug=True)

# 2360 for 3 months , 300mbps
