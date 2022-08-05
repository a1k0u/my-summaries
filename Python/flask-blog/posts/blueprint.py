from flask import Blueprint
from flask import render_template
from flask import redirect
from models import Post
from models import Tag

posts = Blueprint("posts", __name__, template_folder="templates")


@posts.route("/")
def index():
    __posts = Post.query.all()
    webpage_title = "Index page"
    page_title = "Posts"
    return render_template(
        "posts/posts.html",
        webpage_title=webpage_title,
        page_title=page_title,
        posts=__posts,
    )


@posts.route("/<url>")
def post_content(url: str):
    post = Post.query.where(Post.url == url).first()
    return render_template("posts/post_content.html", post=post, tags=post.tags)


@posts.route("/tag/<url>")
def tag_content(url: str):
    tag = Tag.query.filter(Tag.url == url).first()
    webpage_title = tag.name
    page_title = f"Posts for '{tag.name}' tag"
    return render_template(
        "posts/posts.html",
        webpage_title=webpage_title,
        page_title=page_title,
        posts=tag.posts,
    )
