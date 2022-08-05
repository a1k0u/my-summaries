from flask import Blueprint
from flask import render_template
from flask import redirect
from models import Post

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/")
def index():
    __posts = Post.query.all()
    return render_template("posts/index.html", posts=__posts)


@posts.route("/<url>")
def post_content(url: str):
    post = Post.query.where(Post.title == url).first()
    return render_template("posts/post_content.html", post=post)
